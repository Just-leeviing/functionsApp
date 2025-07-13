FUNCTION_TEMPLATES = [
    {
        "name": "add_numbers",
        "inputs": [{"name": "a", "type": "int"}, {"name": "b", "type": "int"}],
        "outputs": [{"name": "result", "type": "int"}],
        "description": "Add two integers"
    },
    {
        "name": "to_string", 
        "inputs": [{"name": "value", "type": "int"}],
        "outputs": [{"name": "text", "type": "str"}],
        "description": "Convert integer to string"
    },
    {
        "name": "get_length",
        "inputs": [{"name": "text", "type": "str"}],
        "outputs": [{"name": "length", "type": "int"}],
        "description": "Get string length"
    },
    {
        "name": "concatenate",
        "inputs": [{"name": "a", "type": "str"}, {"name": "b", "type": "str"}],
        "outputs": [{"name": "result", "type": "str"}],
        "description": "Concatenate two strings"
    },
    {
        "name": "multiply",
        "inputs": [{"name": "a", "type": "int"}, {"name": "b", "type": "int"}],
        "outputs": [{"name": "result", "type": "int"}],
        "description": "Multiply two integers"
    },
    {
        "name": "split_string",
        "inputs": [{"name": "text", "type": "str"}, {"name": "delimiter", "type": "str"}],
        "outputs": [{"name": "parts", "type": "list"}],
        "description": "Split string by delimiter"
    },
    {
        "name": "filter_positive",
        "inputs": [{"name": "numbers", "type": "list"}],
        "outputs": [{"name": "positive", "type": "list"}],
        "description": "Filter positive numbers"
    },
    {
        "name": "format_text",
        "inputs": [{"name": "template", "type": "str"}, {"name": "value", "type": "int"}],
        "outputs": [{"name": "formatted", "type": "str"}],
        "description": "Format text with value"
    }
]
