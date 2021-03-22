add_library(Problem STATIC problem.cu problem.cuh)
set_target_properties(Problem PROPERTIES POSITION_INDEPENDENT_CODE TRUE)
target_include_directories(Problem PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
