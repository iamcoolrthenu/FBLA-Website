const nodemailer = require('nodemailer');

// SMTP server configuration
let transporter = nodemailer.createTransport({
    host: "smtp.tolibsanni.tech",
    port: ***REMOVED***,
    secure: false, // true for 465, false for other ports
    auth: {
        user: "***REMOVED***",
        pass: "***REMOVED***",
    },
});

// Email options
let mailOptions = {
    from: '"Tolib Sanni" <***REMOVED***>',
    to: "***REMOVED***",
    subject: "Node.js Email Test",
    text: "This is a test email sent from Node.js.",
    html: "<b>This is a test email sent from Node.js.</b>",
};

// Send the email
transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
        return console.log(error);
    }
    console.log('Message sent: %s', info.messageId);
});