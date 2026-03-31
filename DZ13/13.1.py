def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
    result = ''
    inside_tag = False
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            result += char

    lines = [line.strip() for line in result.split('\n') if line.strip()]
    result = '\n'.join(lines)
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(result)
delete_html_tags('draft.html', 'result.txt')