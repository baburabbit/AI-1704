% Diet suggestions for diabetes
diet_suggestion(diabetes, [
    avoid(sugar),
    limit(carbohydrates),
    focus(on_proteins),
    eat(vegetables),
    control_portion_size
]).

% Diet suggestions for hypertension
diet_suggestion(hypertension, [
    reduce(sodium_intake),
    eat(potassium_rich_foods),
    limit(caffeine),
    choose(lean_proteins),
    control_portion_size
]).

% Rule to get diet suggestions based on disease
get_diet_suggestions(Disease, Suggestions) :-
    diet_suggestion(Disease, Suggestions).
