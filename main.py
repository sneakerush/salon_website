from flask import Flask, render_template, url_for

# debugging - terminal
# flask --app main.py --debug run  

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():

    return render_template('home.html')


@app.route('/book')
def book():
    # haircut/price
    haircuts = {
        'Add on Cut w/ Color': '$80.00',
        'Child Haircut': '$20.00',
        'Conditioning Haircut': '$60.00',
        'Women Cut & Style': '$80.00',
        'Luxury Blowout': '$100.00',
        'Shampoo & Blowdry': '$140.00',
        'Curls Only (No shampoo)': '$40.00',
        'Formal Style (no shampoo)': '$80.00',
        'Bang Trim': '$25.00',
        'Beard Trim': '$15.00',
        "Men's Cut": '$30.00',
    }


    return render_template('book.html', haircuts=haircuts)



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/staff')
def staff():
    staff_names = [
    'Carol Johnson', 'Jane Smith', 'Terra Castro', 'Sarah Davis', 
    'Jenna Smith', 'Christina Soar', 'Tabitha Prisc', 'Jewels Reese', 'Scarlet Rivers'
    ]
    social_links = {
        staff_names[0] : {
            'instagram': 'https://www.instagram.com/mike__stark',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555',
        },
        staff_names[1] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
        staff_names[2] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
        staff_names[3] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
        staff_names[4] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
        staff_names[5] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
        staff_names[6] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
        staff_names[7] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
        staff_names[8] : {
            'instagram': 'https://www.instagram.com/pewdiepie',
            'facebook': 'https://www.facebook.com/michael.stark.1276/',
            'twitter': 'https://twitter.com/sneakerush',
            'phone': 'Tel: 954-789-8555'
        },
    }

    staff_imgs = {
        staff_names[0]: '/static/images/IMG_0853.jpg',
        staff_names[1]: '/static/images/IMG_0854.jpg',
        staff_names[2]: '/static/images/IMG_0855.jpg',
        staff_names[3]: '/static/images/IMG_0856.jpg',
        staff_names[4]: '/static/images/IMG_0857.jpg',
        staff_names[5]: '/static/images/IMG_0858.jpg',
        staff_names[6]: '/static/images/IMG_0859.jpg',
        staff_names[7]: '/static/images/IMG_0861.jpg',
        staff_names[8]: '/static/images/IMG_0862.jpg',

    }

    return render_template('staff.html', staff_names=staff_names, social_links=social_links, staff_imgs=staff_imgs)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()