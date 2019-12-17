#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_tools"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/sanjeev/tb3_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/sanjeev/tb3_ws/install/lib/python3/dist-packages:/home/sanjeev/tb3_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/sanjeev/tb3_ws/build" \
    "/usr/bin/python3" \
    "/home/sanjeev/tb3_ws/src/open_manipulator_with_tb3_tools/setup.py" \
    build --build-base "/home/sanjeev/tb3_ws/build/open_manipulator_with_tb3_tools" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/sanjeev/tb3_ws/install" --install-scripts="/home/sanjeev/tb3_ws/install/bin"
