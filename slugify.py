def slugify():
    """
    A finction that makes a perfect slug for websites
    :return:
    """
    title = input('Enter your title: ')
    slug = title.strip().replace(' ','-').lower()
    while '--' in slug:
        final_slug = slug.replace('--','-')
    # slug = title.lower().replace(' ','-')
        return final_slug
# print(slugify())

print(slugify.__doc__)