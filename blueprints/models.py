from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mudar123**",
    database="devweb01"
) 

cursor = db.cursor()