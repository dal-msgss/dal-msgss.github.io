---
speaker: Ethan O'Connell
date: 2026-03-23
title: Classification of Missingness for Extreme Wave Surge Modelling
---
A common approach to modelling extreme wave surges is the block maxima approach, where the yearly maximum surge levels are extracted and modelled using the generalized extreme value distribution. Sea level records typically have many missing observations which can lead to biased estimation if the true yearly maxima are unobserved. Several methods have been proposed to account for missing observations within the block maxima approach, but their performance often depends on the missingness mechanism of the underlying series.

A crucial component of extreme surge modelling in the presence of missing data is the estimation of the probability that the observed block maxima correspond to the true block maxima. This can be framed as a semi-supervised classification problem, where the labels are only known for the fully observed years. In this talk, we will present an overview of the block maxima method for modelling extreme wave surges in Atlantic Canada and discuss data augmentation methods to develop classifiers by inducing missingness on the fully observed years.
