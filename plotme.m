function hi = plotme(de)
% argument is system of diff eqs called like plotme(@sysdes) in the
% matlab cmd line
t = [0:0.001:15]; %time variable
for ii = -3:1:3 %the following for loops are just to obtain coordinates for initial condition vector a
    for jj = -6:2:6
        a = [ii, jj]; %init conds x,y in phase space
        [t, y] = ode45(de, t, a);
         plot(y(:,1), y(:, 2))
         hold on
    end
end


[x, y] = meshgrid(-4:1:4, -10:1:10); %This is for the velocity vector field overlay since it may not
u = y;                               %be totally apparent where solutions move over time
v = -x - 4* (x.^2 - 1) .* y;
quiver(x,y,u,v,2.5)