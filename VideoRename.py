import os,shutil



main_path = r'C:\rail_share\images\11bg21\test1\1403\9\8'


# new_path = r'C:\rail_share\images\11bg21\test1\1403\9\7'


files = os.listdir(main_path)



for h_file in files:

    list_m_files = os.listdir(os.path.join(main_path,h_file))

    for m_file in list_m_files:


        movie_files = os.listdir(os.path.join(main_path,h_file,m_file))


        for movie_file in movie_files:

            print(movie_file)

            new_name = movie_file.split('_')

            date = new_name[0].split('-')

            new_name[0] = f'{date[0]}-{date[1]}-08'

            new_name = f'{new_name[0]}_{new_name[1]}_{new_name[2]}_{new_name[3]}_{new_name[4]}'
            print(new_name)


            # if not os.path.exists(new_name):
            #     os.makedirs(new_name)

            # new_name = os.path.join(new_path,h_file,m_file,new_name)


            movie_path = os.path.join(main_path,h_file,m_file,movie_file)
            new_name = os.path.join(main_path,h_file,m_file,new_name)

            os.rename(movie_path,new_name)

            # shutil.copy(movie_path,new_name)


            # os.rename()