#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:09:48 2020

@author: Aman 
"""
from tkinter import *
import numpy as np
import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from pandas import DataFrame
import ttk
from tkFileDialog import askopenfilename
from tkinter.ttk import Separator, Style
import MajorCities
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


base_url = "https://api.waqi.info"

# read secret token from file containing the token as a single string
# you need to create this file if you want to reproduce this analysis
token = open('waqitoken.txt').read()


import pandas as pd

class MyWindow(tk.Tk):

    def __init__(self):
        
        tk.Tk.__init__(self)
        
        
        self.title("COVID Air Polluton Tracker - Team Transcendentals")
        
        #Entry
        #self.e1=tk.Entry(self)
        #self.e1.grid(row=3, column=6, sticky=tk.EW)
        #self.e1.insert(0, 'Taiping')
        
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(4, weight=1, uniform='a')
        
        #Labels
        self.title=tk.Label(self, text='COVID Air Pollution Tracker', bg='blue', fg='white')
        self.title.config(font=('times new roman', 30))
        self.title.grid(row=0, column=0, columnspan=5, sticky=tk.EW)
        
        self.title=tk.Label(self, text='Variation with Time')
        self.title.config(font=('times new roman', 20))
        self.title.grid(row=3, column=0, columnspan=1, sticky=tk.EW)
        
        self.title=tk.Label(self, text='Compare Cities')
        self.title.config(font=('times new roman', 20))
        self.title.grid(row=3, column=2, columnspan=1, sticky=tk.EW)
        
        self.title=tk.Label(self, text='Get Live Data')
        self.title.config(font=('times new roman', 20))
        self.title.grid(row=3, column=4, columnspan=1, sticky=tk.EW)

        self.title=tk.Label(self, text='INSTRUCTIONS\n 1. Click on Load Data to upload data file as per format in AQICN database.\n2. Use City Name from the dropdown and click on Plot Button.\n 3. Use the 2nd Plot to add the data for comparison.\n 4. Use Clear Button to clear the comparison plot.\n 5. See realtime AQI data for major cities from the dropdown.')
        self.title.config(font=('times new roman', 12, 'bold'))
        self.title.grid(row=10, column=0, columnspan=5, sticky=tk.EW)
        
        self.title=tk.Label(self, text='Created By: Transcendentals [Aman, Nidhish, Ashish, Yash]', bg='grey95')
        self.title.config(font=('times new roman', 12))
        self.title.grid(row=12, column=0, columnspan=5, sticky=tk.EW)
        
        self.title=tk.Label(self, text='Good: 0-50\n Satisfactory: 51-100\n Moderately Polluted: 101-200\n Poor: 201-300\n Very Poor: 301-400\n Severe: 410-500')
        self.title.config(font=('times new roman', 18))
        self.title.grid(row=8, column=4, columnspan=1, sticky=tk.NSEW)
        
        #Separators
        self.sep = Separator(self, orient="horizontal")
        self.sep.grid(column=0, row=1, columnspan=5, sticky=tk.EW)
        self.sty = Style(self)
        self.sty.configure("TSeparator", background="red")
        
        self.sep = Separator(self, orient="horizontal")
        self.sep.grid(column=0, row=7, columnspan=5, sticky=tk.EW)
        self.sty = Style(self)
        self.sty.configure("TSeparator", background="red")
        
        self.sep = Separator(self, orient="horizontal")
        self.sep.grid(column=0, row=9, columnspan=5, sticky=tk.EW)
        self.sty = Style(self)
        self.sty.configure("TSeparator", background="red")
     
        self.sep = Separator(self, orient="horizontal")
        self.sep.grid(column=0, row=11, columnspan=5, sticky=tk.EW)
        self.sty = Style(self)
        self.sty.configure("TSeparator", background="red")
                
        self.sep = Separator(self, orient="vertical")
        self.sep.grid(column=1, row=3, rowspan=7, sticky=tk.NS)
        self.sty = Style(self)
        self.sty.configure("TSeparator", background="red")
        
        self.sep = Separator(self, orient="vertical")
        self.sep.grid(column=3, row=3, rowspan=7, sticky=tk.NS)
        self.sty = Style(self)
        self.sty.configure("TSeparator", background="red")


        #Buttons
        self.button1 = tk.Button(text='LOAD DATA', command=self.load)
        self.button1.grid(row=2, column=0, columnspan=5, sticky=tk.NSEW)
        
        self.button3 = tk.Button(text='PLOT', command=self.myplot)
        self.button3.grid(row=4, column=0, rowspan=1, sticky=tk.NSEW)
        
        self.button2 = tk.Button(text='CLEAR', command=self.clearplot)
        self.button2.grid(row=5, column=2, rowspan=1, sticky=tk.NSEW)
        
        self.button4 = tk.Button(text='PLOT', command=self.myplot2)
        self.button4.grid(row=4, column=2, rowspan=1, sticky=tk.NSEW)
        
        self.button5 = tk.Button(text='GET LATEST AQI', command=self.updatelivedata)
        self.button5.grid(row=5, column=4, rowspan=1, sticky=tk.EW)
        
        #Plot
        fig, (self.ax1) = plt.subplots(nrows=1, ncols=1, sharey = False)
        fig1, (self.ax2) = plt.subplots(nrows=1, ncols=1, sharey = False)

        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.get_tk_widget().grid(row=6, column=0, rowspan=3, columnspan=1, sticky=tk.NSEW)
        
        self.canvas1 = FigureCanvasTkAgg(fig1, self)
        self.canvas1.get_tk_widget().grid(row=6, column=2, rowspan=3, columnspan=1, sticky=tk.NSEW)
        '''
        #Toolbar
        self.toolbarFrame = tk.
        toolbarFrame.grid(row=22,column=4)
        toolbar = NavigationToolbar2TkAgg(canvas, toolbarFrame)
        '''
        
        self.livedata()

    def load(self):

        name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xlsx'))])

        if name:
            if name.endswith('.csv'):
                self.df = pd.read_csv(name)
                self.df1 = pd.DataFrame(data=self.df)
            else:
                self.df = pd.read_excel(name)
                self.df1 = pd.DataFrame(data=self.df)
        
        self.updatecity()
         
     
    def myplot(self):
        self.ax1.cla()
        city = self.variable.get()        
        x=self.df1.loc[self.df1['City'] == city, 'Date']
        y=self.df1.loc[self.df1['City'] == city, 'median']
        x = x.values
        y = y.values
        
        plt.scatter(x,y) 
        plt.show()

        data2 = {'x': x,
             'y': y}
        
        df2 = DataFrame(data2,columns=['x','y'])

        df2 = df2[['x','y']].groupby('x').sum()
        
        b=df2.plot(kind='line', legend=True, ax=self.ax1, color='r',marker='o', fontsize=10)
        self.ax1.axvspan('12/15/2019', max(x), color='red', alpha=0.2)
        
        self. ax1.legend(['Cities']) 
        self.ax1.set_xlabel('Time')
        self.ax1.set_ylabel('Parameter')
        self.ax1.set_title('Pollutant Parameter Vs. Time')
        
        self.ax1.plot()       
        
        self.canvas.draw()
        
    def myplot2(self):
        city = self.variable.get()        
        x=self.df1.loc[self.df1['City'] == city, 'Date']
        y=self.df1.loc[self.df1['City'] == city, 'median']
        x = x.values
        y = y.values
        
        plt.scatter(x,y) 
        plt.show()

        data2 = {'x': x,
             'y': y}
        
        df2 = DataFrame(data2,columns=['x','y'])

        df2 = df2[['x','y']].groupby('x').sum()
        b=df2.plot(kind='line', legend=True, ax=self.ax2,marker='o', fontsize=10)

        self.ax2.legend(['Cities']) 
        self.ax2.set_xlabel('Time')
        self.ax2.set_ylabel('Parameter')
        self.ax2.set_title('Pollutant Parameter Vs. Time')
        
        self.canvas1.draw() 
        
        
        
    def updatecity(self):
        
        temp=self.df1.groupby(['City']).mean()    
        self.OPTIONS=temp.index.values
        self.variable = tk.StringVar(self)
        self.variable.set(self.OPTIONS[0]) # default value
        self.e2 = tk.OptionMenu(self, self.variable, *self.OPTIONS)
        self.e2.grid(row=5, column=0, sticky=tk.EW)
        
    def livedata(self):
        self.OPTIONS=MajorCities.livecity
        self.variable1 = tk.StringVar(self)
        self.variable1.set("None") # default value
        self.e2 = tk.OptionMenu(self, self.variable1, *self.OPTIONS)
        self.e2.grid(row=4, column=4, sticky=tk.NSEW)
    
    def updatelivedata(self):
        city = self.variable1.get()
        r = requests.get(base_url + "/feed/" + city + "/?token=" + token)
        q = "Air quality index: {}".format(r.json()['data']['aqi'])
        self.label1=tk.Label(self, text=q)
        self.label1.config(font=('times new roman', 20))
        self.label1.grid(row=6, column=4, columnspan=1, sticky=tk.NSEW)
        
    def clearplot(self):
        self.ax2.cla()
        self.canvas1.draw() 

if __name__ == '__main__':
    app = MyWindow()
    app.mainloop()
