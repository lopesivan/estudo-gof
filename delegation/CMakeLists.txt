cmake_minimum_required(VERSION 3.3)
project(delegation)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp Shape.h Rectangle.cpp Rectangle.h Window.cpp Window.h Circle.cpp Circle.h)
add_executable(delegation ${SOURCE_FILES})