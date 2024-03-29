# Install script for directory: /home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/sanjeev/tb3_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sanjeev/tb3_ws/build/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/catkin_generated/installspace/open_manipulator_with_tb3_gazebo.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_with_tb3_gazebo/cmake" TYPE FILE FILES
    "/home/sanjeev/tb3_ws/build/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/catkin_generated/installspace/open_manipulator_with_tb3_gazeboConfig.cmake"
    "/home/sanjeev/tb3_ws/build/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/catkin_generated/installspace/open_manipulator_with_tb3_gazeboConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_with_tb3_gazebo" TYPE FILE FILES "/home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_with_tb3_gazebo" TYPE DIRECTORY FILES
    "/home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/config"
    "/home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/launch"
    "/home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/models"
    "/home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_simulations/open_manipulator_with_tb3_gazebo/worlds"
    )
endif()

