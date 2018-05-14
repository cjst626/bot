var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// Initialize Discord Bot
var bot = new Discord.Client({
   token: auth.token,
   autorun: true
});
bot.on('ready', function (evt) {
    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(bot.username + '#' + 9334 + ' - (' + bot.id + 438758839672635404 + ')');
});
bot.on('message', function (user, userID, channelID, message, evt) {
    // Our bot needs to know if it will execute a command
    // It will listen for messages that will start with `!`
    if (message.substring(0, 1) == '!') {
        var args = message.substring(1).split(' ');
        var cmd = args[0];
       
        args = args.splice(1);
        switch(cmd) {
            // !Rat_King
            case 'Rat_King':
                bot.sendMessage({
                    to: channelID,
                    message: 'https://www.youtube.com/watch?v=9qwsLxb2IlY !'
                });
                break;

            //!Ledgend_of_Acrius
            case 'Ledgend_of_Acrius':
                bot.sendMessage({
                    to: channelID,
                    message: 'https://www.youtube.com/watch?v=K_jBXm1zXJY !'
                });
                break;
            //!Sturm_and_Drang
            case 'Sturm_and_Drang':
                bot.sendMessage({
                    to: channelID,
                    message: 'https://www.youtube.com/watch?v=XT0Fs-9Owcg !'
                });
                break;
 
            //!Mida_Multi_Tool
            case 'Mida_Multi_Tool':
                bot.sendMessage({
                    to: channelID,
                    message: 'https://www.youtube.com/watch?v=Br6Btji0otE !'
                });
                break;
            //!commands
            case 'commands':
                bot.sendMessage({
                        to: channelID,
                        message: '!Rat_King, !Ledgend_of_Acrius, !Sturm_and_Drang, and !Mida_Multi_Tool'
                });
                break;
        }
    }
});
