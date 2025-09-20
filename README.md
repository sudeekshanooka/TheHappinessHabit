# The Happiness Habit 🌟

A web application that helps users track and celebrate their daily happy memories through an interactive calendar interface and SMS messaging system powered by Twilio.

## 🎯 What is this project?

The Happiness Habit is designed to help people cultivate daily positivity by making it easy to record and reflect on happy moments. Users interact with a beautiful calendar interface where they can add memories, while the SMS integration sends gentle daily prompts asking "What made you smile today?" to encourage regular reflection on positive experiences.

## ✨ Key Features

- **📅 Interactive Calendar**: A beautiful calendar interface to view and add happy memories by date
- **📱 SMS Integration**: Sends daily prompts via Twilio SMS asking about positive moments
- **💭 Memory Tracking**: Add and store happy memories that can be viewed on specific calendar dates
- **📱 Responsive Design**: Clean, user-friendly interface that works across all devices
- **🔄 Two-way SMS**: Receive and process user responses to SMS prompts

## 🛠️ Built With

- **Backend**: Python Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **SMS Service**: Twilio API for messaging
- **Styling**: Font Awesome icons, custom responsive CSS

## 📁 Project Overview

```
TheHappinessHabit/
├── extraConctent.py        # Main Flask application with web interface
├── main.py                 # Simple SMS sending script
├── getUserMsg.py           # SMS response handler
├── sms.py                  # SMS utility functions (development)
├── requirements.txt        # Python dependencies
├── index.html              # Main calendar interface
├── static/
│   ├── css/               # Custom stylesheets
│   └── js/                # JavaScript functionality
├── templates/
│   ├── images/            # Logo and image assets
│   └── hidden.html        # SMS webhook template
└── myproject/             # Python virtual environment
```

## 🚀 How it Works

The application combines a web-based calendar interface with SMS messaging to create a complete happiness tracking experience. Users can add memories directly through the calendar, while the Twilio integration enables automated daily prompts and response collection via SMS.

## 💡 Purpose

This project was created to help people develop a habit of noticing and recording positive moments in their daily lives. By providing both visual (calendar) and text-based (SMS) interaction methods, it makes happiness tracking accessible and convenient.

## ⚙️ Technical Implementation

- **Flask Backend**: Handles web routes, SMS webhooks, and message processing
- **Calendar Interface**: Interactive JavaScript calendar for memory management
- **Twilio Integration**: Bidirectional SMS communication for prompts and responses
- **Responsive Design**: Mobile-friendly interface that works on all devices

## 🔧 Dependencies

Built with Python Flask and includes dependencies for Twilio SMS integration, web templating, and HTTP handling. See `requirements.txt` for the complete list of packages including Flask, Twilio SDK, and supporting libraries.

## 🌱 Future Potential

The project provides a foundation for expanding into features like user authentication, persistent data storage, analytics dashboards, and mobile applications. The modular structure makes it easy to extend and customize for different use cases.