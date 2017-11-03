from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
	

	
@app.route("/injectionTime", methods = ['POST'])
def injectionTime():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	movieYear = request.form['injectionMovieYear']
	select_stmt = (
        "select * from Movie where MovieYear = " + movieYear 
		)
	cursor.execute(select_stmt)
	movies = cursor.fetchall()
	cnx.close()
	return render_template('injection.html', movies=movies)
	
@app.route("/employeeIndex")
def employeeIndex():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	select_stmt = ("Select * from Movie group by MovieName")
	cursor.execute(select_stmt)
	mMovies = cursor.fetchall()
	
	cursor = cnx.cursor()
	select_stmt = ("Select * from Genre group by Genre,Movie_idMovie")
	cursor.execute(select_stmt)
	mGenre = cursor.fetchall()
	
	cursor = cnx.cursor()
	select_stmt = ("Select * from TheatreRoom")
	cursor.execute(select_stmt)
	mRoom = cursor.fetchall()
	
	cursor = cnx.cursor()
	select_stmt = ("Select * from Showing group by ShowingDateTime,idShowing")
	cursor.execute(select_stmt)
	mShowing = cursor.fetchall()
	
	cursor = cnx.cursor()
	select_stmt = ("Select * from Customer group by LastName,idCustomer")
	cursor.execute(select_stmt)
	mCustomer = cursor.fetchall()
	
	cursor = cnx.cursor()
	select_stmt = ("Select Attend.Rating, Attend.Showing_idShowing, Customer.FirstName, " 
	"Customer.LastName, Showing.ShowingDateTime, Movie.MovieName, "
	"Movie.idMovie from Attend inner join Customer on Customer.idCustomer = "
	"Attend.Customer_idCustomer inner join Showing on Attend.Showing_idShowing = "
	"Showing.idShowing inner join Movie on Showing.Movie_idMovie = Movie.idMovie"
	" group by Attend.Rating, Attend.Showing_idShowing, Customer.FirstName, "
	"Customer.LastName, Showing.ShowingDateTime, Movie.MovieName, "
	"Movie.idMovie"
	)
	cursor.execute(select_stmt)
	mAttend = cursor.fetchall()
	
	return render_template('employeeIndex.html', movies = mMovies, genres = mGenre, 
		rooms = mRoom, showings = mShowing, customers = mCustomer, attends = mAttend)
		
'''
---------------------------------------------------------------------------------------
'''
		
@app.route("/movieModify", methods= ["POST"])
def movieModify():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idMovie = request.form['movieModifyIdMovie']
	movieName = request.form['movieModifyMovieName']
	movieYear = request.form['movieModifyMovieYear']
	select_stmt = (
        "update Movie set MovieName = \"" + movieName + "\", MovieYear = " + movieYear +
		" where idMovie = " + idMovie
	)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/movieDelete", methods= ["POST"])
def movieDelete():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idMovie = request.form['movieDeleteIdMovie']
	select_stmt = (
        "delete from Movie where idMovie = " + idMovie
	)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/movieAdd", methods=["POST"])
def movieAdd():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idMovie = request.form['movieAddIdMovie']
	movieName = request.form['movieAddMovieName']
	movieYear = request.form['movieAddMovieYear']
	select_stmt = (
        "insert into Movie (idMovie, MovieName, MovieYear) values (" + idMovie + ","
		+ "\"" + movieName + "\"," + movieYear + ")" )
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
'''
---------------------------------------------------------------------------------------
'''
	
@app.route("/genreDelete", methods=["POST"])
def genreDelete():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idMovie = request.form['genreDeleteIdMovie']
	genre = request.form['genreDeleteGenre']
	select_stmt = (
        "delete from Genre where Genre = \"" + genre + "\" and Movie_idMovie = "
		+ idMovie 
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/genreAdd", methods=["POST"])
def genreAdd():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idMovie = request.form['genreAddIdMovie']
	genre = request.form['genreAddGenre']
	select_stmt = (
        "insert into Genre (Genre, Movie_idMovie) values (\"" + genre + "\","
		+ idMovie + ")"
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
'''
---------------------------------------------------------------------------------------
'''
	
@app.route("/roomModify", methods = ["POST"])
def roomModify():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	roomID = request.form['roomModifyRoomId']
	capacity = request.form['roomModifyCapacity']
	select_stmt = (
        "update TheatreRoom set Capacity = " + capacity + " where RoomNumber = "
		+ roomID
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/roomAdd", methods = ["POST"])
def roomAdd():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	roomID = request.form['roomAddRoomId']
	capacity = request.form['roomAddCapacity']
	select_stmt = (
        "insert into TheatreRoom (RoomNumber,Capacity) values (" + roomID + 
		"," + capacity + ")"
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/roomDelete", methods = ["POST"])
def roomDelete():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	roomID = request.form['roomDeleteRoomId']
	select_stmt = (
        "delete from TheatreRoom where RoomNumber = " + roomID 
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
'''
---------------------------------------------------------------------------------------
'''

@app.route("/showingModify",methods = ["POST"])
def showingModify():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idShowing = request.form['showingModifyIdShowing']
	dateTime = request.form['showingModifyShowingDateTime']
	idMovie = request.form['showingModifyIdMovie']
	idRoom = request.form['showingModifyIdRoom']
	price = request.form['showingModifyTicketPrice']
	select_stmt = (
        "update Showing set ShowingDateTime = \'" + dateTime + "\', Movie_idMovie = " +
		idMovie + ", TheatreRoom_RoomNumber = " + idRoom + ", TicketPrice = " + price
		+ " where idShowing = " + idShowing
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/showingDelete",methods = ["POST"])
def showingDelete():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idShowing = request.form['showingDeleteIdShowing']
	select_stmt = (
        "delete from Showing where idShowing = " + idShowing 
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/showingAdd",methods = ["POST"])
def showingAdd():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idShowing = request.form['showingAddIdShowing']
	dateTime = request.form['showingAddShowingDateTime']
	idMovie = request.form['showingAddIdMovie']
	idRoom = request.form['showingAddIdRoom']
	price = request.form['showingAddTicketPrice']
	select_stmt = (
        "insert into Showing (idShowing, ShowingDateTime, Movie_idMovie," +
		"TheatreRoom_RoomNumber, TicketPrice) values (" + idShowing + "," +
		"\'" + dateTime + "\'," + idMovie + "," + idRoom + "," + price + ")"
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()

'''
---------------------------------------------------------------------------------------
'''
@app.route("/customerModify",methods = ["POST"])
def customerModify():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idCustomer = request.form['customerModifyIdCustomer']
	firstName = request.form['customerModifyFirstName']
	lastName = request.form['customerModifyLastName']
	emailAddress = request.form['customerModifyEmailAddress']
	sex = request.form['customerModifySex']
	select_stmt = (
        "update Customer set FirstName = \"" + firstName + "\", LastName = \"" +
		lastName + "\", EmailAddress = \"" + emailAddress + "\", Sex = \"" + sex
		+ "\" where idCustomer = " + idCustomer
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()

	
@app.route("/customerDelete",methods = ["POST"])
def customerDelete():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idCustomer = request.form['customerDeleteIdCustomer']
	select_stmt = (
        "delete from Customer where idCustomer = " + idCustomer 
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
@app.route("/customerAdd",methods = ["POST"])
def customerAdd():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	idCustomer = request.form['customerAddIdCustomer']
	firstName = request.form['customerAddFirstName']
	lastName = request.form['customerAddLastName']
	emailAddress = request.form['customerAddEmailAddress']
	sex = request.form['customerAddSex']
	select_stmt = (
        "insert into Customer (idCustomer,FirstName,LastName,EmailAddress"
		",Sex) values (" + idCustomer + ",\"" + firstName + "\",\"" + lastName + 
		"\",\"" + emailAddress + "\",\"" + sex + "\")"
		)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return employeeIndex()
	
	
'''
####################################################################################
'''

@app.route("/customerIndex")
def customerIndex():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	select_stmt = (
        "Select distinct ShowingDateTime from Showing"
	)
	cursor.execute(select_stmt)
	mDates = cursor.fetchall()
	cnx.close()
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	select_stmt = (
        "Select distinct Genre from Genre"
	)
	cursor.execute(select_stmt)
	mGenres = cursor.fetchall()
	cnx.close()
	return render_template('customerIndex.html', genres=mGenres, dates = mDates)
	
@app.route("/searchShowing", methods = ["POST"])
def searchShowing():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	genre = request.form['selectGenre']
	start = request.form['selectStartDate']
	end = request.form['selectEndDate']
	openSeats = request.form.getlist('openSeats')
	movieTitle = request.form['movieTitle']
	select_stmt = (
        "Select distinct Showing.idShowing, Showing.ShowingDateTime, Movie.MovieName,"
		" Showing.TheatreRoom_RoomNumber, Showing.TicketPrice from Showing inner join Movie" 
		" on Movie.idMovie = Showing.Movie_idMovie inner join Genre on Genre.Movie_idMovie = "
		"Showing.Movie_idMovie where Genre = \"" + genre + "\" and ShowingDateTime >= \'"
		+ start + "\' and ShowingDateTime <= \'" + end + "\' and Movie.MovieName = \"" + 
		movieTitle + "\""
	)
	if openSeats:
		select_stmt = (
        "SELECT distinct Showing.idShowing, Showing.ShowingDateTime, Movie.MovieName, Showing.TheatreRoom_RoomNumber, Showing.TicketPrice"
" FROM Showing INNER JOIN Movie ON Movie.idMovie = Showing.Movie_idMovie INNER JOIN Genre ON Genre.Movie_idMovie = Showing.Movie_idMovie INNER JOIN"
" TheatreRoom ON TheatreRoom.RoomNumber = Showing.TheatreRoom_RoomNumber LEFT JOIN (SELECT Attend.Showing_idShowing, count(*) as Tickets_Purchased FROM Attend"
" GROUP BY Attend.Showing_idShowing) A ON A.Showing_idShowing = Showing.idShowing WHERE (A.Tickets_Purchased < TheatreRoom.Capacity OR A.Tickets_Purchased is null)"
" and Genre =\"" + genre + "\" and ShowingDateTime >= \'" + start + "\' and ShowingDateTime <= \'" + end + "\' and Movie.MovieName = \"" + movieTitle + "\""
" GROUP BY Showing.idShowing, TheatreRoom.Capacity UNION"
" SELECT distinct Showing.idShowing, Showing.ShowingDateTime, Movie.MovieName, Showing.TheatreRoom_RoomNumber, Showing.TicketPrice"
" FROM Showing INNER JOIN Movie ON Movie.idMovie = Showing.Movie_idMovie INNER JOIN Genre ON Genre.Movie_idMovie = Showing.Movie_idMovie INNER JOIN TheatreRoom"
" ON TheatreRoom.RoomNumber = Showing.TheatreRoom_RoomNumber RIGHT JOIN (SELECT Attend.Showing_idShowing, count(*) as Tickets_Purchased FROM Attend GROUP BY"
" Attend.Showing_idShowing) A ON A.Showing_idShowing = Showing.idShowing WHERE (A.Tickets_Purchased < TheatreRoom.Capacity OR A.Tickets_Purchased is null)"
" and Genre =\"" + genre + "\" and ShowingDateTime >= \'" + start + "\' and ShowingDateTime <= \'" + end + "\' and Movie.MovieName = \"" + movieTitle + "\""
" GROUP BY Showing.idShowing, TheatreRoom.Capacity"
	)
	cursor.execute(select_stmt)
	result = cursor.fetchall()
	cnx.close()
	return render_template('searchShowing.html', result = result)

@app.route("/buyTicket", methods = ["POST"])
def buyTicket():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	first = request.form['firstName']
	last = request.form['lastName']
	ID = request.form['showingID']
	select_stmt = (
        "insert into Attend (Customer_idCustomer,Showing_idShowing) values ((select "
		"idCustomer from Customer where FirstName = \"" + first + "\" and LastName = \""
		+ last + "\")," + ID + ")"
	)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return render_template('customerIndex.html');

@app.route("/rateShowing", methods = ["POST"])
def rateShowing():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	first = request.form['firstName']
	last = request.form['lastName']
	ID = request.form['showingID']
	rating = request.form['rating']
	select_stmt = (
        "update Attend set Rating = " + rating + " where Showing_idShowing = " +
		ID + " and Customer_idCustomer in (Select idCustomer from Customer where " +
		"FirstName = \"" + first +
		"\" and LastName = \"" +  last + "\")"
	)
	cursor.execute(select_stmt)
	cnx.commit()
	cnx.close()
	return render_template('customerIndex.html');	

@app.route("/allShowing", methods = ["POST"])
def allShowing():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	first = request.form['firstName']
	last = request.form['lastName']
	select_stmt = (
        "select Movie.MovieName, Attend.Rating from Attend inner join Showing on " +
		"Attend.Showing_idShowing = Showing.idShowing inner join Movie on Movie.idMovie" +
		"= Showing.Movie_idMovie where Customer_idCustomer in (select idCustomer from" +
		" Customer where FirstName = \"" + first +
		"\" and LastName = \"" +  last + "\")"
	)
	cursor.execute(select_stmt)
	movies = cursor.fetchall()
	cnx.close()
	return render_template('allShowing.html', users=movies)

@app.route("/profile", methods = ["POST"])
def profile():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	first = request.form['firstName']
	last = request.form['lastName']
	select_stmt = (
        "Select * from  Customer where FirstName = \"" + first +
		"\" and LastName = \"" +  last + "\" "
	)
	cursor.execute(select_stmt)
	user = cursor.fetchall()
	cnx.close()
	return render_template('profile.html', results=user)
	
	
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)