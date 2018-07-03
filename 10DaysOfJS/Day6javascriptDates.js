function getDayName(dateString) {
    let dayName = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    // The test uses MM/DD/YYYY date format so use getUTCDay() method which will give us
    // the day in numeric format, sunday is 0, monday is 1, etc. use that to index our dayName
    // array which has Sunday as our 0 index.
    const i = (new Date(dateString)).getUTCDay();
    return dayName[i];
}
