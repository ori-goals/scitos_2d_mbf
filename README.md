# scitos_2d_mbf
Move Base Flex configuration files for  2D navigation stack on a Metralab SCITOS G5/A5 robot base. 


To test this, you can do the following:

 1. Install the STRANDS codebase via "Using the L-CAS repository" - https://github.com/LCAS/rosdistro/wiki
 2. Install the simulator `sudo apt-get install ros-kinetic-strands-morse`
 3. Add https://github.com/ori-goals/scitos_2d_mbf amd https://github.com/strands-project/scitos_2d_navigation to your catkin workspace, then rebuild
 4. Run the MORSE simulator for the environment of your choosing, e.g. `roslaunch strands_morse tsc_morse.launch`
 5. Run scitos_2d_mbf with the corresponding map: 
 ```
 roslaunch scitos_2d_mbf scitos_2d_mbf.launch map:=`rospack find strands_morse`/tsc/maps/tsc.yaml  no_go_map:=`rospack find strands_morse`/tsc/maps/tsc_nogo.yaml with_no_go_map:=true
 ```
 6. Provide a navigation goal via RViz.

