```
function x_dot = aircraft_dynamics(t, x, u, disturbance)
    % x = [altitude; velocity; flight path angle]
    % u = [thrust; pitch angle]
    % disturbance = [wind disturbance; turbulence effect]
    
    g = 9.81;  % Gravity (m/s^2)
    m = 5000;  % Aircraft mass (kg)
    S = 30;    % Wing area (m^2)
    rho = 1.225; % Air density at sea level (kg/m^3)
    CD0 = 0.02; % Drag coefficient at zero lift
    CL = 0.5;   % Lift coefficient (assumed constant)

    % Disturbances
    wind = disturbance(1);  
    turbulence = disturbance(2);
    
    % State variables
    altitude = x(1);  
    velocity = x(2);
    gamma = x(3);  % Flight path angle (radians)

    % Inputs
    thrust = u(1);   
    pitch_angle = u(2);  
    
    % Drag force
    drag = 0.5 * rho * velocity^2 * S * (CD0 + CL^2 / (pi * 10));  % Simplified drag equation
    
    % Aircraft dynamics equations
    x_dot = zeros(3,1);
    x_dot(1) = velocity * sin(gamma); % Altitude rate of change
    x_dot(2) = (thrust - drag) / m - g * sin(gamma); % Velocity rate of change
    x_dot(3) = (thrust * sin(pitch_angle)) / (m * velocity) - g / velocity * cos(gamma); % Flight path angle rate of change

    % Adding external disturbances
    x_dot(2) = x_dot(2) + wind;  % Modify velocity with wind disturbance
    x_dot(3) = x_dot(3) + turbulence;  % Modify angle with turbulence disturbance
end
```
```
% MPC settings
N = 20;  % Prediction horizon
Ts = 1;  % Sampling time (seconds)

% Define weights
w1 = 1;  % Weight for fuel consumption
w2 = 10; % Weight for trajectory deviation
w3 = 0.1; % Weight for control effort

% Initial conditions
x0 = [1000; 200; 0];  % [altitude (m), velocity (m/s), flight path angle (rad)]
u0 = [5000; 0];       % Initial thrust and pitch angle

% Set up constraints
u_min = [0; -0.1];    % Minimum thrust and pitch angle
u_max = [10000; 0.1]; % Maximum thrust and pitch angle

% External disturbance (wind and turbulence)
disturbance = [0; 0];

% Desired altitude and velocity
x_ref = [1500; 250; 0];  % Reference altitude, velocity, and angle

% Simulation loop
T_sim = 100;  % Total simulation time
x = x0;
u = u0;

for t = 0:Ts:T_sim
    % Solve the optimization problem (quadratic programming or another solver)
    u_opt = mpc_control(x, N, x_ref, w1, w2, w3, u_min, u_max, disturbance);
    
    % Update system state using aircraft dynamics
    [t_step, x_next] = ode45(@(t, x) aircraft_dynamics(t, x, u_opt, disturbance), [0 Ts], x);
    x = x_next(end, :)';  % Take the final state from the ODE solver
    
    % Apply the control input
    u = u_opt;
    
    % Display or store results (altitude, velocity, etc.)
    disp(['Time: ', num2str(t), ' Altitude: ', num2str(x(1)), ' Velocity: ', num2str(x(2))]);
end
```
```
function u_opt = mpc_control(x, N, x_ref, w1, w2, w3, u_min, u_max, disturbance)
    % Define the optimization variables and constraints here
    % For simplicity, this can be solved using fmincon or a quadratic solver.
    
    % Placeholder: Optimize control input
    u_opt = fmincon(@(u) cost_function(x, u, x_ref, N, w1, w2, w3), ...
                    [5000; 0], [], [], [], [], u_min, u_max);
end

function J = cost_function(x, u, x_ref, N, w1, w2, w3)
    % Define the cost function for MPC
    fuel_consumption = w1 * abs(u(1));  % Simplified fuel model
    deviation = w2 * norm(x - x_ref)^2; % Penalize deviation from the reference
    control_effort = w3 * norm(u)^2;    % Penalize aggressive control

    J = fuel_consumption + deviation + control_effort;
end
```
