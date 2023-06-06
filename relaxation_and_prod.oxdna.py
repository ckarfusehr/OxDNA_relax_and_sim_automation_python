#!/home/ckarfusehr/anaconda3/envs/OxDNA/bin/python3.10
## Author: Christoph Karfusehr
## input files provided by Elija Feigl
## Goal is to propperly equilibrate a DNA structure in OxDNA, followed by a normal simulation.

## Imports
import oxpy
import os

def auto_detect_files():
	"""
	Auto detection of input files
	"""
	#global topology, initial_conf, forces, use_autodetect_files
	topology, initial_conf, forces = "None", "None", "None"
	files_in_dir = os.listdir()
	for file in files_in_dir:
		if file[-4:] == ".top":
			topology = file
		elif (".dat" in file) | (".conf" in file):
			initial_conf = file
		elif ((".frc" in file)) | (file == "external_forces.txt") | (file == "output_force.frc"):
			forces = file
		
	print(f"Continue with detected input files? (y/n)\nTopology: {topology}\nConformation: {initial_conf}\nForces: {forces}")
	use_autodetect_files = True
	if input() == "n":
		use_autodetect_files = False
	return topology, initial_conf, forces, use_autodetect_files

def dialog(use_autodetect_files, topology, initial_conf, forces):
	"""
	Interact with user to set up relaxation and pot. simulation.
	"""
	use_force_file = False
	
	if use_autodetect_files == False:
		print(f"Name of topology file?")
		topology = input()

		print(f"Name of conformation file?")
		initial_conf = input()

	print(f"Do initial relaxation? (y/n)")
	do_initial_relax = False
	if input() == "y":
		do_initial_relax = True

		print(f"Use forces from force file? (y/n)")
		if input() == "y":
			use_force_file = True
			if use_autodetect_files == False:
				print(f"Name of force file?")
				forces = input()

	print(f"Continue with normal OxDNA sim? (y/n)")
	continue_with_sim = False
	if input() == "y":
		continue_with_sim = True
	return use_force_file, continue_with_sim, topology, initial_conf, forces, do_initial_relax

## Relaxation procedures
def monte_carlo(topology, initial_conf, forces, use_force_file):
	"""
	Monte Carlo with opt. forces
	"""
	with oxpy.Context():
		relax_1 = oxpy.InputFile()
		relax_1.init_from_filename("relax1.oxdna.inp")
		relax_1["topology"] = topology	
		relax_1["conf_file"] = initial_conf
		if use_force_file == True:
			relax_1["external_forces"] = "true"
			relax_1["external_forces_file"] = forces

		# Run
		manager1 = oxpy.OxpyManager(relax_1)
		manager1.run(int(relax_1["steps"]))
	return

def md_mod_backbone(topology, forces, use_force_file):
	"""
	Molecular dynamics with opt. forces and modified backbone potential (?)
	"""
	with oxpy.Context():
		relax_2 = oxpy.InputFile()
		relax_2.init_from_filename("relax2.oxdna.inp")
		relax_2["topology"] = topology
		if use_force_file == True:
			relax_2["external_forces"] = "true"
			relax_2["external_forces_file"] = forces
		
		# Run
		manager2 = oxpy.OxpyManager(relax_2)
		manager2.run(int(relax_2["steps"]))
	return

def md(topology):
	"""
	Molecular dynamics
	"""
	with oxpy.Context():
		relax_3 = oxpy.InputFile()
		relax_3.init_from_filename("relax3.oxdna.inp")
		relax_3["topology"] = topology

		# Run
		manager3 = oxpy.OxpyManager(relax_3)
		manager3.run(int(relax_3["steps"]))
	return

## Production runs
def oxdna_production(topology, continue_with_sim):
	"""
	OxDNA simulation of (hopefully) relaxed structure
	"""
	if continue_with_sim:
		with oxpy.Context():
			oxdna_sim = oxpy.InputFile()
			oxdna_sim.init_from_filename("production.oxdna.inp")
			oxdna_sim["topology"] = topology

			# Run
			manager_sim = oxpy.OxpyManager(oxdna_sim)
			manager_sim.run(int(oxdna_sim["steps"]))
	return

def main():
	topology, initial_conf, forces, use_autodetect_files = auto_detect_files()
	use_force_file, continue_with_sim, topology, initial_conf, forces, do_initial_relaxation = dialog(use_autodetect_files, topology, initial_conf, forces)
	print(f"Alright, let shit hit the fan")
	if do_initial_relaxation:
		monte_carlo(topology, initial_conf, forces, use_force_file)
		print(f"Done with relax steps 1/3")
		md_mod_backbone(topology, forces, use_force_file)
		print(f"Done with relax steps 2/3")
		md(topology)
		print(f"Done with relax steps 3/3")
	if continue_with_sim:
		oxdna_production(topology, continue_with_sim)
		print(f"Done with oxdna simulation")
	return

main()
