while True:
    s = input('Input your Github directory name: ')

    if not s.startswith('P'):
        print('The name must starts with P !')
        continue

    name_list = s.split('-')
    if len(name_list) != 3:
        print('The name must be like P25000-Beijing-Wei !')
        continue

    if name_list != [x.capitalize() for x in name_list]:
        print('Every word must be capitalized !')
        continue

    print('Good boy~ You can use {}'.format(s))
    break
