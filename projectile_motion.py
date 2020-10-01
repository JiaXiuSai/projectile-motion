# 07/04/2019
# Project - Projectile motion simulation
#-------------------------------------------------------------------------

# Import modules.

import os
import datetime
import math
import matplotlib.pyplot as plt
import csv
import time
from graphics import *
#-------------------------------------------------------------------------

# Functions 

# Checks if value input by user is resonable/float.
def get_float(prompt,default,minimum,maximum):
	
	value_test = input(prompt)
	
	# Test if the value input is a float.
	try:	
		
		# Test if the value input is reasonable.	
		if(float(value_test)<=maximum):
			
			if(float(value_test)>=minimum):
				
				# Test if the value input is a float.
				answer = float(value_test)
					
				print(" Value recorded.")
				# If the value input is a float, the value is returned back to the main program.
				return answer	
				
			# If the value input is unrealistic, the default value that was set beforehand is returned to the main program.	
			else:
				print(" Oops!  The value of the number is too small. Using default value.")
				return default
				
		# If the value input is unrealistic, the default value that was set beforehand is returned to the main program.	
		else:
			print(" Oops!  The value of the number is too big. Using default value.")
			return default	
			
	# If the value input is not a float, a ValueError will appear and the default value that was set beforehand is returned to the main program.		
	except ValueError:
		print(" Oops!  That was not a valid number. Using default value.")
		return default	
	
# End of function get_float
#-------------------------------------------------------------------------

# Lets the user change the current parameters.
def change_para():

	os.system('cls')
	print (program_info)
	print(" Function: Change parameters")
	print (line*30)
	
	# The parameters are input by user:	
	#	
	# Mass of projectile object (kilograms).
	# Height of initial projection (meters).
	# Initial speed of projectile (meter per second).
	# Frontal area of object (meters square).
	# The step size (seconds).
	# Initial angle (degrees).
	mass = get_float(" Enter the mass of the cannonball in kg (1-20): ",5.5,1,20)
	height = get_float(" Enter the initial height (0-10): ",0,0,10)
	speed = get_float(" Enter the initial speed of the cannonball in m/s (10-200): ",100,10,200) 
	area = get_float(" Enter the frontal area of cannonball in meters\u00b2 (0.005-1): ",0.0154,0.005,1)   
	step = get_float(" Enter the step size in seconds (0.001-1): ",0.01,0.001,1)
	ang_in_deg = get_float(" Enter the initial angle in degrees (10-90): ",45,10,90)
	# The angle is converted from degrees into radians.
	ang_in_rad = math.radians(ang_in_deg)
	
	# Parameters are returned back to the main program.
	return mass,height,speed,area,step,ang_in_deg,ang_in_rad

# End of function change_para
#-------------------------------------------------------------------------	

# Show current parameters input by user.
def show_current_para(mass,height,speed,area,step,ang_in_deg,ang_in_rad):

	os.system('cls')
	print (program_info)
	print(" Function: Show current parameters")
	print (line*30)
	print(" Current parameters of projectile object:")
		
	# Prints the parameters input by user.	
	print(" Mass = %.2f kg" %(mass))
	print(" Height = %.1f meters" %(height))
	print(" Speed = %.2f meters per seconds" %(speed))
	print(" Surface area = %.4f meters\u00b2" %(area))
	print(" Step size = %s seconds" %(step))
	print(" Initial angle = %.2f degrees (%0.2f radians)" %(ang_in_deg,ang_in_rad))
					
# End of function show_current_para
#-------------------------------------------------------------------------

# Calculates the data set using the parameters input by user.
def calculate_data(mass,height,speed,area,step,ang_in_deg,ang_in_rad):

	# Ask if user wants to calculate data.
	print("\n Would you like to run calculations?")
	print("\n 1: Yes\n Press any key to go back to main menu.")
	user_command = input("\n Enter command: ")
		
	# When '1' is input, continue to run function calculate_data.		
	if (user_command =='1'):

		i = int(0)				# Iteration (i.e. step)
		t_current = float(0) 	# Current time value (seconds)
		t_next = float(0)		# Next time value (seconds)
		fd_current = float(0)	# Current air resistance (newtons)
		fd_next	= float(0)		# Next air resistance (newtons)
				
		# Values for X-coordinates:
		x_current = float(0)	# Current distance (meters)
		x_next = float(0)		# Next distance (meters)
		xv_current = float(0)	# Current velocity (meters/seconds)
		xv_next = float(0)		# Next velocity	(meters/seconds)
				
		# Values for Y-coordinates:
		y_current = float(0)	# Current distance (meters)
		y_next = float(0)		# Next distance (meters)
		yv_current = float(0)	# Current velocity (meters/seconds)
		yv_next = float(0)		# Next velocity	(meters/seconds)
				
		v_current = float(0)	# Current velocity (meters/seconds)
		v_next = float(0)		# Next velocity	(meters/seconds)

		# Fixed parameters:
		g = 9.807		# Gravity on Earth (meters/second square)
		drag = 0.47		# Drag coefficient of a ciruclar smooth surface
		a_d = 1.225		# Air density at sea-level (kg/m**3)
				
		# Lists:
		t = []		# Holds time data
		x = []		# Holds distance data for X axis
		y = []		# Holds distance data for Y axis
		xv = []		# Holds velocity data for X axis
		yv = []		# Holds velocity data for Y axis
		v = []		# Holds total velocity data
					
		t_sim_run = float(0)		# Current simulation run time (seconds)
					
		# Set the initial values and add to data lists.
		t.append(0.0)
		x.append(0.0)	
		y.append(height)
		xv.append(speed*math.cos(ang_in_rad))
		yv.append(speed*math.sin(ang_in_rad))
		v.append(speed)
					
		os.system('cls')
		print (program_info)
		print(" Function: Calculate and show current data set")
		print (line*30)
					
		# Title and header of the table.
		print("\n Data table:\n")
		print(" Step|  Time  |  X_Velocity  |  Y_Velocity  |  Velocity  |  X_Distance  |  Y_Distance")
					
		# Loop to create data points.
		i = 0;
					
		# Makes this function run until object lands on the ground.
		while (y_current >= 0):
					
			# Get current values
			t_current = t[i]
			x_current = x[i]
			y_current = y[i]
			xv_current = xv[i]
			yv_current = yv[i]
			v_current = v[i]
						
			# Calculate current gravitational force.
			fg_current = (mass*g)
							
			# Calculate and add current X air resistance to list.
			xfd_current = 0.5*xv_current*abs(xv_current)*drag*area*a_d
							
			# Calculate and add current X acceleration to list.
			xa_current = (xfd_current)/mass
							
			# Calculate and add next X velocity to list.
			xv.append(xv_current - (xa_current*step))
							
			# Calculate and add next X distance to list.
			x.append(x_current + (xv_current*step))
							
			# Calculate current Y air resistance.
			yfd_current = 0.5*yv_current*abs(yv_current)*drag*area*a_d
							
			# Calculate current Y acceleration.
			ya_current = (fg_current + yfd_current)/mass
							
			# Calculate and add next Y velocity to list.
			yv.append(yv_current - (ya_current*step))
							
			# Calculate and add next Y distance to list.
			y.append(y_current + (yv_current*step))
							
			# Get updated values of X velocity and Y velocity.
			xv_current = xv[i+1]
			yv_current = yv[i+1]
						
			# Calculate final velocity using pythagoras theorem.
			v.append(math.sqrt((xv_current*xv_current)+(yv_current*yv_current)))
							
			# Calculate and next time to list.
			t.append(t_current + step)
							
			# Update the simulation run time.
			t_sim_run = t_sim_run + step
							
			# Data table
			print("  %d  |  %.2f  |    %.3f    |   %.3f     |   %.3f  |    %.3f     |    %.3f" %(i,t_current,xv_current,yv_current,v_current,x_current,y_current))
							
			# Update the iteration / step.
			i = i + 1
					
		print (line*30)
					
		# Values in data lists are returned back to main program.
		return i,t,xv,yv,x,y,v
		
# End of function calculate_data
#-------------------------------------------------------------------------

# Analyse the data calculated.
def analyse_data(mass,i,t,xv,yv,x,y,v):
	
	# Checks if any parameters is input by user.
	if (0 < (mass)):
		
		# Checks if data set is calculated.
		num_x=len(x)
		if (0 < num_x):		
				
			# Ask if the user wants to analyses data.
			print("\n Would you like to display analysis?")
			print("\n 1: Yes\n Press any key to go back to main menu.")
			user_command = input("\n Enter command: ")
		
			# When '1' is input, continue to run function calculate_data.		
			if (user_command =='1'):
				
				os.system('cls')
				print (program_info)
				print(" Function: Analyse data")
				print (line*30)
				
				print(" Data analysis:\n")
				
				# Highest height achieved.
				mx = max(x)
				max_x = x.index(mx)
				print(" Furthest distance achieved at:\n X-coordinate - %0.3f meters\n Y-coordinate - %0.3f meters\n Speed - %0.3f meter per seconds \n Time - %0.2f seconds \n" %(mx,y[max_x],v[max_x],t[max_x]))
				
				# Furthest distance achieved.
				my = max(y)
				max_y = y.index(my)
				print(" Highest distance achieved at:\n X-coordinate - %0.3f meters\n Y-coordinate - %0.3f meters\n Speed - %0.3f meter per seconds \n Time - %0.2f seconds " %(x[max_y],my,v[max_y],t[max_y]))
				
				input ("\n Press any key to go back to main menu.")	
		
			return i,t,xv,yv,x,y,v
				
		else:
			os.system('cls')
			print (program_info)
			print(" Function: Analyse data")
			print (line*30)
			print(" No data calculated yet.")
			input ("\nPress any key to go back to main menu.")
				
	# Informs the user to input parameters.		
	else:
		os.system('cls')
		print (program_info)
		print(" Function: Analyse data")
		print (line*30)
		print(" No parameters enter yet.")
		input ("\n Press any key to go back to main menu.")	
	
# End of function analysis_data
#-------------------------------------------------------------------------

# Plots a graph using data set calculated.
def plot_graph(mass,i,t,xv,yv,x,y,v):
	
	# Checks if any parameters is input by user.
	if (0 < (mass)):
		
		# Checks if data set is calculated.
		num_x=len(x)
		if (0 < num_x):
			
			os.system('cls')
			print (program_info)
			print(" Function: Plot graph")
			print (line*30)
			
			# Show commands for different graphs.
			print("\n Commands| Graph:")
			print("    1    | Displacement Y against Displacement X")
			print("    2    | Velocity against Time")
			print("\n Input any key to go back to main menu.")
			
			user_command = input("\n Enter command: ")
			os.system('cls')
			print (program_info)
			print(" Function: Plot graph")
			print (line*30)
			print (" Plotting graph......")
			
			# When '1' is input, display graph: Displacement Y against Displacement X.	
			if (user_command =='1'):
				
				my = max(y)
				max_y = y.index(my)
				maxpoint = [max_y]
				
				# Plot graph with (x-axis,y-axis and line type).
				plt.plot(x,y,'b-x', ms=6, markevery=maxpoint)
				
				# Annotate the highest point on graph.
				my = max(y)
				max_y = y.index(my)
				plt.annotate("(%0.1f , %0.1f)" %(x[max_y],my) ,xy = (0,0), xytext = (x[max_y]*0.8,my*0.8))
				
				# Scale graph.
				plt.axis('scaled')
				
				# X-axis label.
				plt.xlabel('Distance X (m)')
				
				# Y-axis label.
				plt.ylabel('Distance Y (m)')
				
				# Graph title.
				plt.title('Projectile Motion Simulation\nDisplacement Y against Displacement X')
				plt.ion()
				
				# Show graph created.
				plt.show()
				input ("\n Press any key to go back.")
				plt.close()
				
				# Return to function plot_graph.
				plot_graph(mass,i,t,xv,yv,x,y,v)
				
			# When '2' is input, display graph: Velocity against Time.		
			if (user_command =='2'):
				
				# Plot graph with (x-axis,y-axis and line type).
				plt.plot(t,v,'b-')

				# X-axis label
				plt.xlabel('Time (seconds)')
				
				# Y-axis label
				plt.ylabel('Velocity (m/s)')
				
				# Graph title
				plt.title('Projectile Motion Simulation\nVelocity against time')
				plt.ion()
				
				# Show graph created
				plt.show()
				input ("\n Press any key to go back.")
				plt.close()
				
				# Return to function plot_graph.
				plot_graph(mass,i,t,xv,yv,x,y,v)
					
		# Informs the user to use calculate function.	
		else:
			os.system('cls')
			print (program_info)
			print(" Function: Plot graph")
			print (line*30)
			print(" No data calculated yet.")
			input ("\n Press any key to go back to main menu.")
	
	# Informs the user to input parameters.		
	else:
		os.system('cls')
		print (program_info)
		print(" Function: Analyse data")
		print (line*30)
		print(" No parameters enter yet.")
		input ("\n Press any key to go back to main menu.")	

# End of function plot_graph
#-------------------------------------------------------------------------		

# Save data set calculated in a csv file.
def save_data(mass,i,t,xv,yv,x,y,v):
	
	# Checks if any parameters is input by user.
	if (0 < (mass)):
		
		# Checks if data set is calculated.
		num_x=len(x)
		if (0 < num_x):
			
			os.system('cls')
			print (program_info)
			print(" Function: Save data")
			print (line*30)
			
			# Open/create csv filed named "Projectile_Motion.csv' and enable write mode.
			Projectile_Motion_csv = open("Projectile_Motion.csv", "w")
			
			# Write column titles
			Projectile_Motion_csv.write("Step, Time(Seconds), X_Velocity(m/s), Y_Velocity(m/s), Velocity(m/s), X_Distance(m), Y_Distance(m)")
			
			num_t=len(t)
			
			# Runs this function for all data calculated stored in list/arrays.
			for i in range(0,num_t):
				
				# Record data calculated in different coloumns.
				Projectile_Motion_csv.write("\n%d,%.2f,%.3f,%.3f,%.3f,%.3f,%.3f" %(i,t[i],xv[i],yv[i],v[i],x[i],y[i]))
			
			# Close csv file. 
			Projectile_Motion_csv.close()
			
			# Informs user data is saved in file.
			print(" Data is now saved in file name: 'Projectile_Motion.csv'.")
			input ("\n Press any key to go back to main menu.")
			
		# Informs the user to use calculate function.
		else:
			os.system('cls')
			print (program_info)
			print(" Function: Save data")
			print (line*30)
			print(" No data calculated yet.")
			input ("\n Press any key to go back to main menu.")	
				
	# Informs the user to input parameters.		
	else:
		os.system('cls')
		print (program_info)
		print(" Function: Save data")
		print (line*30)
		print(" No parameters enter yet.")
		input ("\n Press any key to go back to main menu.")
		
# End of function save data
#-------------------------------------------------------------------------

# Runs simulation with parameters input by user and the data calculated.	
def run_simu(mass,height,speed,area,step,ang_in_deg,ang_in_rad,i,t,xv,yv,x,y,v):
	
	# Checks if any parameters is input by user.	
	if (0 < (mass)):
		
		# Checks if data set is calculated.
		num_x=len(t)
		if (0 < num_x):
			
			# Determine whether values are possible to display.	
			if (0 >= (height)):
				
				try:
					os.system('cls')
					print (program_info)
					print(" Function: Run simulation")
					print (line*30)
					print (" Running simulation......")
					
					# Run this simulation for speed above speed of 100.	
					if (100 < (speed)):
						scale = 2000
						
					# Run this simulation for speed under speed of 100.		
					if (100 >= (speed)):
						scale = 800
	
					# Run this simulation for speed under speed of 50.	
					if (50 >= (speed)):
						scale = 300
	
					# Set margin size. 
					width_x = 1000
					length_y = 600
					centre_x = width_x/2
					centre_y = length_y/2
					start_x = height+50
					start_y = 500
												
					# Set projectile size.
					radius = 20
					radius_dot = 1
						
					# Print blank margin.
					win = GraphWin("Projectile Motion", width_x, length_y)
					
					# Path of projectile object.
					path = Circle(Point(start_x,start_y), radius_dot)
					path.setFill("#FF8500") 
					path.setOutline("#FF8500") 
					path.draw(win)
											
					# Projectile object.
					ball = Circle(Point(start_x,start_y), radius)
					ball.setFill("#4D4D4D")
					ball.draw(win)

					# Ground.
					ground= Rectangle(Point(0,start_y+radius), Point(width_x,length_y))
					ground.setFill("#53AF23")
					ground.draw(win)
						
					# Cannon 1.
					cannnon_1= Circle(Point(start_x,start_y), radius+5)
					cannnon_1.setFill("#000000")
					cannnon_1.draw(win)
					
					# Cannon 2.
					cannnon_2= Polygon(Point(start_x-15,start_y+15), Point(start_x+30,start_y-45), Point(start_x+55,start_y-15))
					cannnon_2.setFill("#000000")
					path.setOutline("#000000") 
					cannnon_2.draw(win)
						
					# Cannon 3.
					cannnon_3= Circle(Point(start_x,start_y+17),10)
					cannnon_3.setFill("#8C611A")
					path.setOutline("#8C611A") 
					cannnon_3.draw(win)
						
					# Create text area.
					message = Text(Point(centre_x,centre_y-150), 'Press any key to start')
					message.draw(win)
						
					# Create text area 2.
					message_2 = Text(Point(centre_x,centre_y-70), '')
					message_2.draw(win)
						
					# Create text area 3.
					message_3 = Text(Point(centre_x,570),"Mass = %.2f kg  Height = %.1f meters  Surface area = %.4f meters\u00b2  Angle = %.1f degrees  " %(mass,height,area,ang_in_deg,))
					message_3.draw(win)
						
					# Create text area 4.
					message_4 = Text(Point(centre_x,30),"Projectile motion simulation")
					message_4.draw(win)
						
					# Create text area 5.
					message_5 = Text(Point(centre_x+350,centre_y+50)," ")
					message_5.draw(win)
						
					win.getKey()
						
					num_t = len(t)
						
					for i in range(1,num_t):
							
						# Start timing current time.
						start_time = time.time()
							
						# Change text area 1 to show changing parameters of running simulation.
						message.setText("Step=%d  Time=%0.2f seconds  Velocity=%0.2f m/s\nPress any key to stop" %(i,t[i],v[i]))
							
						# Calculate next position for object.
						next_delta_x = x[i]*(width_x/scale)
						next_delta_y = y[i]*(length_y/scale)
						next_x = start_x + next_delta_x
						next_y = start_y - next_delta_y
							
						# Draw path of projectile object.
						new_path = Circle(Point(next_x,next_y), radius_dot)
						new_path.setFill("#FF8500")
						new_path.setOutline("#FF8500") 
						new_path.draw(win)
							
						# Draw projectile object.
						new_ball = Circle(Point(next_x,next_y), radius)
						new_ball.setFill("#4D4D4D")
							
						# Print new object position.
						new_ball.draw(win)

						# Calculate running time for simulation.
						elapsed_time = time.time() - start_time
							
						h = t[i]-t[i-1]

						# Test if simulation is running same speed/ faster than real time. 
						if (elapsed_time < h):
							
							# Slow down simulation if simulation is running too fast.
							time.sleep(h - elapsed_time)
							message_2.setText("Real-time")
							
						# If simulation is too slow, continue running the simulation.	
						else:
								# Inform the user that simulation is not in real time.
								message_2.setText("Not real time")

						# Undraw starting/current object.
						ball.undraw()
						
						# Make new object the current object.
						ball = new_ball
						path = new_path
						
						# End simulation when user press any key.
						keypress = win.checkKey()
						if (keypress !=""):
							break
								
					# Show how long the simulation ran and the highest height achieved.
					mx = max(x)
					max_x = x.index(mx)		
					message.setText("Press any key to exit.\nReal time = %0.2f seconds\n\nHighest distance achieved at :\n X-coordinate - %0.3f meters \n Y-coordinate - %0.3f meters" %(t[i],mx,y[max_x],))

					# Show the furthest distance achieved.
					my = max(y)
					max_y = y.index(my)
					message_5.setText("Furthest distance achieved at:\n X-coordinate - %0.3f meters\n Y-coordinate - %0.3f meters" %(x[max_y],my))
					win.getKey()
					win.close()	
					return()
						
				except:
					print()	
					
			# Informs that values are not able to simulate due to height.		
			else:
				os.system('cls')
				print (program_info)
				print(" Function: Run simulation")
				print (line*30)
				print(" Unable to run simulation")
				input ("\n Press any key to go back to main menu.")	
				
		# Informs the user to use calculate function.	
		else:
			os.system('cls')
			print (program_info)
			print(" Function: Run simulation")
			print (line*30)
			print(" No data calculated yet.")
			input ("\n Press any key to go back to main menu.")
				
	# Informs the user to input parameters.
	else:
		os.system('cls')
		print (program_info)
		print(" Function: Run simulation")
		print (line*30)
		print(" No parameters enter yet.")
		input ("\n Press any key to go back to main menu.")

# End of function run simu.
#-------------------------------------------------------------------------

# MAIN PROGRAM
now = datetime.datetime.now()
program_info = (" DUISC\n Projectile Motion Simulator\n %s:%2.f %s/%s/%s" %(now.hour, now.minute, now.day, now.month, now.year))
menu_options = {}
user_command = "nothing"

# Line used in program.
line ="-"

# Projectile parameters.
mass = 0.0
height = 0.0
speed = 0.0
area = 0.0

# Sim parameters.
step = 0.0
ang_in_rad = 0.0
ang_in_deg = 0.0

# Other variables.
t_0 = 0.0
i = 0.0

# Data list.
t = []	
x = []
y = []					    	
xv = []				
yv = []	
v = []

# Main menu function.
while (user_command != 'quit'):
	
	os.system('cls')
	print (program_info)
	print(" Main menu")
	print (line*30)
	
	# Print main menu and commands available.
	print (" Commands| Functions")
	print (line*30)
	print("    1    | Change parameters")
	print("    2    | Show current parameters")
	print("    3    | Calculate and show current data set")
	print("    4    | Analyse data")	
	print("    5    | Plot graph")
	print("    6    | Save data")
	print("    7    | Run visuals")
	print("   quit  | Quit program")
	
	user_command = input("\nEnter command: ")
	
	# When '1' is input, run function calculate_data.
	if (user_command =='1'):
		mass,height,speed,area,step,ang_in_deg,ang_in_rad = change_para()
			
		# Checks if any parameters is input by user.
		if (0 < (mass)):
			
			try:
				show_current_para(mass,height,speed,area,step,ang_in_deg,ang_in_rad)
				i,t,xv,yv,x,y,v = calculate_data(mass,height,speed,area,step,ang_in_deg,ang_in_rad)
				print(" Number of data points for:")
				print(" Time - %d" %(len(t)-1))
				print(" Velocity - %d" %(len(v)-1))
				print(" X - %d" %(len(x)-1))
				print(" Y - %d" %(len(y)-1))
				print (line*30)
				analyse_data(mass,i,t,xv,yv,x,y,v)
				
			except:
				print()
				
		# If no parameters are input by user yet, no parameters can be displayed.
		else:
			os.system('cls')
			print (program_info)
			print(" Function: Change parameters")
			print (line*30)
			
			# Informs the user to input parameters.
			print("No parameters enter yet.")	
			
			# Stop the function to let the user choose when to exit to main menu.
			input ("\nPress any key to go back to main menu.")
			
	# When '2' is input, run function show current parameters.
	if (user_command =='2'):
		show_current_para(mass,height,speed,area,step,ang_in_deg,ang_in_rad)
			
		# Checks if any parameters is input by user.
		if (0 < (mass)):
			
			try:
				i,t,xv,yv,x,y,v = calculate_data(mass,height,speed,area,step,ang_in_deg,ang_in_rad)
				print(" Number of data points for:")
				print(" Time - %d" %(len(t)-2))
				print(" Velocity - %d" %(len(v)-2))
				print(" X - %d" %(len(x)-2))
				print(" Y - %d" %(len(y)-2))
				print (line*30)
				analyse_data(mass,i,t,xv,yv,x,y,v)
				
			except:
				print()
				
		# If no parameters are input by user yet, no parameters can be displayed.		
		else:
			os.system('cls')
			print (program_info)
			print(" Function: Show current parameters")
			print (line*30)
			
			# Informs the user to input parameters.
			print(" No parameters enter yet.")	
		
			# Stop the function to let the user choose when to exit to main menu.
			input ("\n Press any key to go back to main menu.")
						
	# When '3' is input, run function calculate data.
	if (user_command =='3'):
		
		# Checks if any parameters is input by user.
		if (0 < (mass)):
			
			try:
				i,t,xv,yv,x,y,v = calculate_data(mass,height,speed,area,step,ang_in_deg,ang_in_rad)
				print(" Number of data points for:")
				print(" Time - %d" %(len(t)-2))
				print(" Velocity - %d" %(len(v)-2))
				print(" X - %d" %(len(x)-2))
				print(" Y - %d" %(len(y)-2))
				print (line*30)
				analyse_data(mass,i,t,xv,yv,x,y,v)
				
			except:
				print()
				
		# If no parameters are input by user yet, no parameters can be displayed.		
		else:
			os.system('cls')
			print (program_info)
			print(" Function: Calculate and show current data set")
			print (line*30)
			
			# Informs the user to input parameters.
			print(" No parameters enter yet.")
			input ("\n Press any key to go back to main menu")
							
	# When '4' is input, run function plot graph.		
	if (user_command =='4'):
		analyse_data(mass,i,t,xv,yv,x,y,v)
			
	# When '5' is input, run function plot graph.		
	if (user_command =='5'):
		plot_graph(mass,i,t,xv,yv,x,y,v)
	
	# When '6' is input, run function save data.	
	if (user_command =='6'):
		save_data(mass,i,t,xv,yv,x,y,v)
	
	# When '7' is input, run function run simulation.	
	if (user_command =='7'):
		run_simu(mass,height,speed,area,step,ang_in_deg,ang_in_rad,i,t,xv,yv,x,y,v)
	
	# When 'quit' is input, exit main menu function.	
	if (user_command =='quit'):
		print ()
	
# End of main menu function.
print(" Quitting...") ;
print(" Program has ended") ;
print(" Bye") ;

# End of main program.
#-------------------------------------------------------------------------
