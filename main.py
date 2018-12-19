'''Main page, always run this'''

import userdata
import userinterface
import usersmodule
import account
import timeline

# If having trouble saving items, add users to account???


def main():
    '''Main function'''
    users, posts = userdata.init()
    # initializing = True
    # while initializing:
    #     try:
    #         action = input('Press 1 to create a new account or 2 to '
    #                        'sign into an existing account... > ')
    #         if int(action) == 1:
    #             signed_in = account.create_account(users)
    #             if signed_in:
    #                 initializing = False
    #             else:
    #                 continue
    #         elif int(action) == 2:
    #             if account.sign_in(users):
    #                 initializing = False
    #             else:
    #                 continue
    #     except:
    #         print('Not a valid operation')


    signed_in = account.sign_in('Jordan00', 'jr11', users)
    timeline.timeline(users, posts, signed_in, 1)

    while True:
        # Timeline, add page view
        action = timeline.prompt_for_action()

        if action == 'SIGN OUT':
            userdata.save_users(users)
            userdata.save_posts(posts)
            break

        # elif action == 'TIMELINE':
        #     userinterface.timeline(users, posts, signed_in, 1)

        elif action.isdigit():
            action = int(action)
            timeline.timeline(users, posts, signed_in, action)

        elif action == 'ACCOUNT SETTINGS':
            account.account(signed_in, posts)
            timeline.timeline(users, posts, signed_in, 1)

        elif action == 'USERS':
            # users_module.users_page(users, signed_in)
            usersmodule.users_page(users, posts, signed_in)
            timeline.timeline(users, posts, signed_in, 1)

        elif action == 'POST':
            post = input('Type your post:\n\t>')
            posts.append(timeline.add_post(post, posts, signed_in))
            timeline.timeline(users, posts, signed_in, 1)


if __name__ == '__main__':
    main()

