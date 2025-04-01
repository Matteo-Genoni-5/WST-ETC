%% Testing the template spectra

close all
clear all
clc

% loading spectrum
filename='Kinney-s0';
spectrum_file=load([filename,' - noHeader.dat']);

% extracting lam and flux
lam=spectrum_file(:,1);
flux=spectrum_file(:,2);

% plot
figure()
plot(lam,flux)
grid on
xlabel('\lambda [A]'),ylabel('Flux [erg/s/cm2/A]')
title(filename)