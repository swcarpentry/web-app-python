import jinja2

loader = jinja2.FileSystemLoader(['.'])
environment = jinja2.Environment(loader=loader)
template = environment.get_template('biography.html')

who = 'Beatrice Tinsley'
what = ['Born 1941', 'Died 1981', 'Studied stellar aging']

result = template.render(name=who, facts=what)
print result
