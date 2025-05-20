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
franchise_make: Could use to try and infer make, but that is already provided, so will remove this
high dimension variable.
front_legroom: Will infer vehicle class, from presence of truck bed or not, plus vehicle length, and 
wheelbase. Do not want to run the risk of over-controlling to the point the causal inference doesn't
work.
fuel_tank_volume: Will also be explained by vehicle category more likely, likely has low predictive power
for the causal work.
height: information should be encompassed in body type. I.E using height to infer whether
it is a sedan, SUV, truck, etc.
highway_fuel_economy: Get information on vehicle performance and likely efficiency through
just horsepower given the relationship between the two.
interior_color: This data seems to hold much more than just interior colors. Sometimes it holds just
random characters (!!!), other times it can hold things such as vehicle trime (xDrive35i Premium AWD)
is_certified: Doesn't have any records