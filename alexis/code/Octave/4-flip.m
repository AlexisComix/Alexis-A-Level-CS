close all;
clear all;
clc;

I = imread("mcbg.jpg");
% Flip the dimensions of the y value
I = flipdim(I, 1);

imshow(I);