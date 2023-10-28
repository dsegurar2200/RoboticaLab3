%%

rosinit http://ubuntu:11311/; %Conexi´on con nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creaci´on publicador
velMsg = rosmessage(velPub); %Creaci´on de mensaje

posPub = rospublisher('/turtle1/pose','turtlesim/Pose');
posMsg = rosmessage(posPub);
%%
posMsg.X=2;
send(posPub,posMsg);
pause(1)q
posMsg.Y=5;
pause(1)
%velMsg.Linear.Y = -8; %Valor del mensaje
%send(velPub,velMsg); %Envio
%pause(1)
%%
PosTur=rossubscriber ('/turtle1/pose')
Posicion=receive(PosTur,15);
rosshutdown