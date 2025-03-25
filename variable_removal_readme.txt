These are notes on which variables are being removed due to a lack of suitability for predictive
and causal inference tasks. For causal inference, the variable list will likely need to be reduced
even further to reduce selection bias and accidentally controlling

Reasons for removals:

VIN: Can lead to over-fitting, vehicle identification number. May be able to extract value from Regex at a later date.
bed_height: Only contains NaN and '--'. 
city: Removing due to high dimensionality, could be parsed in the future to generalize to regions.
combine_fuel_economy: The entire column was null
description: Can get other vital information from other variables. Can revisit and attempt to parse in the future
engine_type: Removing this because it holds the exact same information as the engine_cylinders variable.
exterior_color: Removing as there are too many permutations for the analysis that wants to be done. Listing Color is a bette alternative.
franchise_dealer: Could use to try and infer make, but that is already provided, so will remove this
high dimension variable.
