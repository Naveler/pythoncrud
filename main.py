import pymysql
import pymysql.cursors
from app import app as app
from tables import Results, DriverResults
from db_config import mysql
from flask import flash, render_template, request, redirect

@app.route('/new_car')
def add_car_view():
	return render_template('add_car.html')
		
@app.route('/add_car', methods=['POST'])
def add_car():
	conn = None
	cursor = None
	try:		
		_car_name = request.form['inputName']
		_car_year = request.form['inputYear']
		if _car_name and _car_year and request.method == 'POST':
			sql = "INSERT INTO cars(car_name, car_year) VALUES(%s, %s)"
			data = (_car_name, _car_year)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('car added successfully!')
			return redirect('/')
		else:
			return 'Error while adding car'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def view():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)

		cursor.execute("SELECT * FROM cars")
		rows = cursor.fetchall()
		car_table = Results(rows)
		car_table.border = True

		cursor.execute("SELECT * FROM drivers")
		rows = cursor.fetchall()
		driver_table = DriverResults(rows)
		driver_table.border = True

		return render_template('view.html', car_table=car_table, driver_table=driver_table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/edit_car/<int:id>')
def edit_view(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM cars WHERE car_id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit_car.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/update_car', methods=['POST'])
def update_cars():
	conn = None
	cursor = None
	try:		
		_car_name = request.form['inputName']
		_car_year = request.form['inputYear']
		_id = request.form['id']
		# validate the received values
		if _car_name and _car_year and _id and request.method == 'POST':
			sql = "UPDATE cars SET car_name=%s, car_year=%s WHERE car_id=%s"
			data = (_car_name, _car_year, _id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('Cars updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating car'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete_car/<int:id>')
def delete_car(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM cars WHERE car_id=%s", (id,))
		conn.commit()
		flash('car deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		



#driver starts
@app.route('/new_driver')
def add_driver_view():
    return render_template('add_driver.html')


@app.route('/add_driver', methods=['POST'])
def add_driver():
    conn = None
    cursor = None
    try:
        _driver_name = request.form['inputDriverName']
        _driver_lastname = request.form['inputDriverLastname']
        # validate the received values
        if _driver_name and _driver_lastname and request.method == 'POST':
            sql = "INSERT INTO drivers(driver_name, driver_lastname) VALUES(%s, %s)"
            data = (_driver_name, _driver_lastname)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Driver added successfully!')
            return redirect('/')
        else:
            return 'Error while adding driver'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit_driver/<int:id>')
def edit_driver(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM drivers WHERE drivers_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit_driver.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_drivers', methods=['POST'])
def update_driver():
    conn = None
    cursor = None
    try:
        _name = request.form['inputDriverName']
        _lastname = request.form['inputDriverLastname']
        _id = request.form['id']
        # validate the received values
        if _name and _lastname and _id and request.method == 'POST':
            sql = "UPDATE drivers SET driver_name=%s, driver_lastname=%s WHERE drivers_id=%s"
            data = (_name, _lastname, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Driver updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating driver'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_driver/<int:id>')
def delete_driver(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM drivers WHERE drivers_id=%s", (id,))
        conn.commit()
        flash('driver deleted successfully!')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run()