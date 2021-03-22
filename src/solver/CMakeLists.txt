add_library(parallelDP STATIC parallelDP.cu parallelDP.cuh)
set_target_properties(parallelDP PROPERTIES POSITION_INDEPENDENT_CODE TRUE)
target_include_directories(parallelDP PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_library(serialDP STATIC serialDP.cu serialDP.cuh)
set_target_properties(serialDP PROPERTIES POSITION_INDEPENDENT_CODE TRUE)
target_include_directories(serialDP PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
