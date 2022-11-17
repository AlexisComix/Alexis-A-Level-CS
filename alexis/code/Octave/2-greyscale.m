close all;
clear all;
clc;
I = imread("mcbg.jpg");

greyscale = I(:,:,1) + I(:,:,2) + I(:,:,3);

figure(1);
imshow(greyscale);
