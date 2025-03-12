def sandwitch(*ingredients):
    print("\nMaking a sanndwich with the following ingredients:")
    for ingredient in ingredients:
        print("-" + ingredient)

sandwitch('cheese')
sandwitch('cheese','tomato')
sandwitch('cheese','tomato','olives')