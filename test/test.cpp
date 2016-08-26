#include <iostream>
#include <gflags/gflags.h>

DEFINE_bool(testarg, false, "Test argument");

int main(int argc, char** argv)
{
    gflags::ParseCommandLineFlags(&argc, &argv, true);

    if(FLAGS_testarg == false)
        std::cout << "Success!" << std::endl;
    else
        std::cout << "Failure!" << std::endl;

    return 0;
}
