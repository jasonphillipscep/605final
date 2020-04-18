function xdot = sysdes(t,x)
%This m-file contains the system of odes
xdot = [x(2); -x(1) - 4 * (x(1)^2 - 1) * x(2)];
