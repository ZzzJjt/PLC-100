
% Distillation column model parameters (assumed values)
A = [-0.5, 0.1; 0.05, -0.3]; % System matrix
B = [0.2; 0.1];               % Input matrix
C = [1, 0];                   % Output matrix (measure temperature of tray 1)
D = 0;                        % Direct transmission

% Continuous-time state-space model
sys = ss(A, B, C, D);

% Discretize the model for use in MPC (sample time Ts = 1 sec)
Ts = 1;
sys_d = c2d(sys, Ts);

% Define constraints (operational limits)
u_min = 0;     % Minimum feed rate
u_max = 1;     % Maximum feed rate
y_min = 100;   % Minimum temperature (operational lower bound)
y_max = 200;   % Maximum temperature (operational upper bound)

% Initial state of the system
x0 = [150; 120]; % Initial tray temperatures

% Define the MPC controller
mpcobj = mpc(sys_d, Ts);

% Prediction horizon and control horizon
mpcobj.PredictionHorizon = 10; % Predict over 10 steps
mpcobj.ControlHorizon = 2;     % Optimize over the next 2 steps

% Constraints on the control input (feed rate) and output (temperature)
mpcobj.MV.Min = u_min;
mpcobj.MV.Max = u_max;
mpcobj.OV.Min = y_min;
mpcobj.OV.Max = y_max;

% Weights for the cost function (minimize output deviations and control effort)
mpcobj.Weights.ManipulatedVariables = 0.1;  % Penalize large control moves
mpcobj.Weights.ManipulatedVariablesRate = 0.01; % Penalize rate of change
mpcobj.Weights.OutputVariables = 1;  % Emphasize tracking of temperature setpoint

% Simulation parameters
Tf = 50;  % Simulation duration (50 seconds)
r = 180 * ones(Tf, 1);  % Setpoint for the temperature (180 degrees)

% Simulate the closed-loop system
x = x0;  % Initial state
u = zeros(Tf, 1);  % Control inputs
y = zeros(Tf, 1);  % Outputs (tray temperatures)

for k = 1:Tf
    % Compute the optimal control action using MPC
    u(k) = mpcmove(mpcobj, x, r(k));

    % Simulate the system's response to the control input
    x = A * x + B * u(k);  % Update states (continuous model)
    y(k) = C * x + D * u(k);  % Compute output (tray temperature)
end

% Display the results
fprintf('Final output temperature: %.2f\n', y(Tf));
fprintf('Final feed rate: %.2f\n', u(Tf)); 
