import functions_framework
@functions_framework.http
def multiplication_http(request):
"""HTTP Cloud Function.
    Args:
        a  - the a value
        b  - the b value
    Returns:
        The computed value
    """
    return a*b