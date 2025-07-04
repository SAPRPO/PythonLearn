#change list in function
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design= unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)



def show_completed_models(completed_models):
    print("\nCompleted models have been printed:")
    for cm in completed_models:
        print(cm)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)