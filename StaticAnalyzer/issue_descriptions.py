#first element is description
#second element is long description
MANIFEST_ISSUE_DESCRIPTIONS = {
  "unprotectedService" : [
    "Service ({service:s}) is not Protected.{perm:s}[android:exported=true]",
    "A service was found to be shared with other apps on the device without an intent filter or a permission requirement therefore leaving it accessible to any other application on the device."
  ],
  "debugEnabled" : [
    "Debug Enabled For App [android:debuggable=true]",
    "Debugging was enabled on the app which makes it easier for reverse engineers to hook a debugger to it. This allows dumping a stack trace and accessing debugging helper classes."
  ],
  "backupEnabled" : [
    "Application Data can be Backed up [android:allowBackup=true]",
    "This flag allows anyone to backup your application data via adb. It allows users who have enabled USB debugging to copy application data off of the device."
  ],
  "backupFlagMissing" : [
    "Application Data can be Backed up [android:allowBackup] flag is missing.",
    "The flag [android:allowBackup] should be set to false. By default it is set to true and allows anyone to backup your application data via adb. It allows users who have enabled USB debugging to copy application data off of the device."
  ],
  "testModeEnabled" : [
    "Application is in Test Mode [android:testOnly=true]",
    "It may expose functionality or data outside of itself that would cause a security hole."
  ],
  "taskAffinitySet" : [
    "TaskAffinity is set for Activity ({item:s})",
    "If taskAffinity is set, then other application could read the Intents sent to Activities belonging to another task. Always use the default setting keeping the affinity as the package name in order to prevent sensitive information inside sent or received Intents from being read by another application."
  ],
  "nonStandardLauchMode" : [
    "Launch Mode of Activity ({item:s}) is not standard.",
    "An Activity should not be having the launch mode attribute set to \"singleTask/singleInstance\" as it becomes root Activity and it is possible for other applications to read the contents of the calling Intent. So it is required to use the \"standard\" launch mode attribute when sensitive information is included in an Intent."
  ],
  "sharedThing" : [
    "{itmname:s} ({item:s}) is not Protected.{perm:s} [android:exported=true]",
    "A {ad:s} {itmname:s} was found to be shared with other apps on the device therefore leaving it accessible to any other application on the device."
  ],
  "sharedThingIntent" : [
    "{itmname:s} ({item:s}) is not Protected. An intent-filter exists.",
    "A {ad:s} {itmname:s} was found to be shared with other apps on the device therefore leaving it accessible to any other application on the device. The presence of intent-filter indicates that the {itmname:s} is explicitly exported."
  ],
  "contentProviderPerms" : [
    "Improper Content Provider Permissions {path:s}",
    "A content provider permission was set to allows access from any other app on the device. Content providers may contain sensitive information about an app and therefore should not be shared."
  ],
  "dialerCode" : [
    "Dailer Code: {xmlhost:s} Found [android:scheme=\"android_secret_code\"]",
    "A secret code was found in the manifest. These codes, when entered into the dialer grant access to hidden content that may contain sensitive information."
  ],
  "smsReceiver" : [
    "Data SMS Receiver Set on Port: {dataport:s} Found[android:port]",
    "A binary SMS recevier is configured to listen on a port. Binary SMS messages sent to a device are processed by the application in whichever way the developer choses. The data in this SMS should be properly validated by the application. Furthermore, the application should assume that the SMS being received is from an untrusted source."
  ],
  "intentPriority" : [
    "High Intent Priority ({value:s})[android:priority]",
    "By setting an intent priority higher than another intent, the app effectively overrides other requests."
  ],
  "activityPriority" : [
    "High Action Priority ({value:s})[android:priority]",
    "By setting an action priority higher than another action, the app effectively overrides other requests."
  ]
}

#Code Review Description
#first element is description
#second is long description
CODE_ISSUES={
  'd_sensitive' : [
    "Files may contain hardcoded sensitive informations like usernames, passwords, keys etc.",
    None
  ],
  'd_ssl': [
    'Insecure Implementation of SSL. Trusting all the certificates or accepting self signed certificates is a critical Security Hole.',
    None
  ],
  'd_sqlite': [
    'App uses SQLite Database. Sensitive Information should be encrypted.',
    None
  ],
  'd_con_world_readable':[
    'The Object is World Readable. Any App can read from the Object',
    None
  ],
  'd_con_world_writable':[
    'The Object is World Writable. Any App can write to the Object',
    None
  ],
  'd_con_private':[
    'App can write to App Directory. Sensitive Information should be encrypted.',
    None
  ],
  'd_extstorage': [
    'App can read/write to External Storage. Any App can read data written to External Storage.',
    None
  ],
  'd_jsenabled':[
    'Insecure WebView Implementation. Execution of user controlled code in WebView is a critical Security Hole.',
    None
  ],
  'd_webviewdisablessl':[
    'Insecure WebView Implementation. WebView ignores SSL Certificate Errors.',
    None
  ],
  'd_webviewdebug': [
    'Remote WebView debugging is enabled.',
    None
  ],
  'dex_debug': [
    'DexGuard Debug Detection code to detect wheather an App is debuggable or not is identified.',
    None
  ],
  'dex_debug_con': [
    'DexGuard Debugger Detection code is identified.',
    None
  ],
  'dex_debug_key': [
    'DecGuard code to detect wheather the App is signed with a debug key or not is identified.',
    None
  ],
  'dex_emulator': [
    'DexGuard Emulator Detection code is identified.',
    None
  ],
  'dex_root': [
    'DexGuard Root Detection code is identified.',
    None
  ],
  'dex_tamper' : [
    'DexGuard App Tamper Detection code is identified.',
    None
  ],
  'dex_cert' : [
    'DexGuard Signer Certificate Tamper Detection code is identified.',
    None
  ],
  'd_ssl_pin': [
    'This App uses an SSL Pinning Library (org.thoughtcrime.ssl.pinning) to prevent MITM attacks in secure communication channel.',
    None
  ],
  'd_root' : [
    'This App may request root (Super User) privileges.',
    None
  ],
  'd_rootcheck' : [
    'This App may have root detection capabilities.',
    None
  ],
  'rand' : [
    'The App uses an insecure Random Number Generator.',
    None
  ],
  'log' : [
    'The App logs information. Sensitive information should never be logged.',
    None
  ],
  'insecure_http' : [
    'App uses insecure web addresses to communicate',
    'Application is using insecure http addresses, request content can be intercepted, using https addresses prevents this'
  ]
}

