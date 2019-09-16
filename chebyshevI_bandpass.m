function Hd = chebyshevI_bandpass(order,fs,low,high)
%BANDPASS_FILTER Returns a discrete-time filter object.

% MATLAB Code
% Generated by MATLAB(R) 9.4 and Signal Processing Toolbox 8.0.
% Generated on: 08-Nov-2018 12:03:16

% Chebyshev Type I Bandpass filter designed using FDESIGN.BANDPASS.

% All frequency values are in Hz.

Apass  = 1;           % Passband Ripple (dB)


% Construct an FDESIGN object and call its CHEBY1 method.
h  = fdesign.bandpass('N,Fp1,Fp2,Ap', order, low, high, Apass, fs);
Hd = design(h, type);

