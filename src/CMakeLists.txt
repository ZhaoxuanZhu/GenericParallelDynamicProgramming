add_subdirectory(problem)
add_subdirectory(solver)

find_package(pybind11 REQUIRED)
pybind11_add_module(dp_solver wrapper.cu)
target_link_libraries(dp_solver PUBLIC parallelDP serialDP ${CONAN_LIBS})