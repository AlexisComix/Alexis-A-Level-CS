close all;
clear all;
clc;
I = imread("mcbg.jpg");

greyscale = (0.299 * I(:,:,1)) + (0.587 * I(:,:,2)) + (0.114 * I(:,:,3));

figure(1);
imshow(greyscale);