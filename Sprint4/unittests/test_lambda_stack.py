import pytest
from aws_cdk import core
from sprint4.hello_lambda_stack import HelloLambdaStack
def test_lambda_stack():
    app = core.App()
    HelloLambdaStack(app,"sairateststack")
    stack_templete=app.synth().get_Stack_by_name('sairateststack').template
    function=[resources for resources in stack_templete['Resources'].value() if resources['type']== 'AWS::Lambda::Function']
    assert len(function)==3

