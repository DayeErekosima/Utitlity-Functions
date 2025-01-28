def random_guesser(inputs):
    import numpy as np
    """ Creates a numpy array that generates 'No' and 'Yes' at random for number of values matching the input data frame

    Args:
        inputs (Boolean): 'No' and 'Yes

    Returns:
        Boolean: 'No' and 'Yes'
    """
    return np.random.choice(['No', 'Yes'], len(inputs))



def all_no(inputs):
    import numpy as np
    """ Creates a numpy array that generates 'No' for number of values matching the input data frame

    Args:
        inputs (Boolean): 'No'

    Returns:
        Boolean: 'No'
    """
    return np.full(len(inputs), 'No')


def all_yes(inputs):
    import numpy as np
    """ Creates a numpy array that generates 'Yes' for number of values matching the input data frame

    Args:
        inputs (Boolean): 'Yes'

    Returns:
        Boolean: 'Yes'
    """
    return np.full(len(inputs), 'Yes')