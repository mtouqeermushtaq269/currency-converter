# currency-converter
This code creates a currency converter application using Python and the Tkinter GUI library. The application uses the exchange rates API to get the latest currency conversion rates.
Here's a breakdown of how the code works:
1.	The necessary libraries (requests and tkinter) are imported.
2.	A Tkinter window is created, with a title of "Currency Converter", a size of 300x400, and a dark blue background.
3.	A custom style is created using the ttk library, which sets the foreground and background colors and font styles for the various GUI elements (labels, text entry fields, buttons, etc.).
4.	The exchange rates for various currencies are retrieved using the API provided by 'https://api.exchangerate-api.com/v4/latest/USD' and stored in a dictionary called 'rates'.
5.	The list of available currencies is created by converting the dictionary keys to a list.
6.	Labels and text entry fields are created for the amount to be converted, the source currency, the target currency, and the converted amount. Comboboxes are created for the source and target currencies, which allow the user to select from the available currencies.
7.	Two functions are defined, one for converting the currency and another for resetting the input fields. The convert_currency() function takes the amount, source currency, and target currency as input, and calculates the converted amount using the rates dictionary. The result is then displayed in the result_label. If the user inputs an invalid value, an error message is displayed instead. The reset_values() function simply clears the input fields and resets the comboboxes to their default values.
8.	Two buttons are created for converting the currency and resetting the input fields.
9.	The mainloop() function is called to run the application and display the GUI window. The program waits for the user to interact with the GUI elements, and executes the corresponding functions when the buttons are clicked.

