# Try to find GFLAGS
# Once done, this will define
#
# GFLAGS_FOUND        - system has GFLAGS
# GFLAGS_INCLUDE_DIRS - GFLAGS include directories
# GFLAGS_LIBRARIES    - libraries need to use GFLAGS

find_path(
	GFLAGS_INCLUDE_DIR
	NAMES gflags/gflags.h
	PATHS ${CONAN_INCLUDE_DIRS_GFLAGS}
)

find_library(
	GFLAGS_LIBRARY
	NAMES gflags 
	PATHS ${CONAN_LIB_DIRS_GFLAGS}
)

set(GFLAGS_FOUND TRUE)
set(GFLAGS_INCLUDE_DIRS ${GFLAGS_INCLUDE_DIR})
set(GFLAGS_LIBRARIES ${GFLAGS_LIBRARY})

mark_as_advanced(GFLAGS_LIBRARY GFLAGS_INCLUDE_DIR)
