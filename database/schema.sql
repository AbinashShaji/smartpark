
DROP TABLE IF EXISTS access_logs;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS parking_prediction_data;
DROP TABLE IF EXISTS parking_slots;
DROP TABLE IF EXISTS parking_locations;
DROP TABLE IF EXISTS admins;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password_hash TEXT NOT NULL,
    is_verified INTEGER DEFAULT 0,
    status TEXT DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    status TEXT DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE parking_locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    description TEXT,
    total_slots INTEGER DEFAULT 0,
    status TEXT DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE parking_slots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parking_location_id INTEGER NOT NULL,
    slot_number TEXT NOT NULL,
    vehicle_type TEXT NOT NULL,
    vehicle_category TEXT,
    status TEXT DEFAULT 'AVAILABLE',
    section_floor TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parking_location_id) REFERENCES parking_locations (id)
);

CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    parking_location_id INTEGER NOT NULL,
    parking_slot_id INTEGER NOT NULL,
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    vehicle_number TEXT NOT NULL,
    vehicle_type TEXT NOT NULL,
    vehicle_category TEXT,
    vehicle_capacity TEXT,
    booking_status TEXT DEFAULT 'PENDING',
    payment_status TEXT DEFAULT 'PENDING',
    qr_token TEXT,
    otp_hash TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (parking_location_id) REFERENCES parking_locations (id),
    FOREIGN KEY (parking_slot_id) REFERENCES parking_slots (id)
);

CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_method TEXT,
    transaction_reference TEXT,
    status TEXT DEFAULT 'PENDING',
    paid_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE parking_prediction_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parking_location_id INTEGER NOT NULL,
    timestamp_date TIMESTAMP NOT NULL,
    hour INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL,
    total_slots INTEGER NOT NULL,
    occupancy INTEGER NOT NULL,
    available_slots INTEGER NOT NULL,
    predicted_occupancy INTEGER,
    predicted_available_slots INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parking_location_id) REFERENCES parking_locations (id)
);

CREATE TABLE notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    type TEXT,
    is_read INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE access_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    access_type TEXT NOT NULL,
    action TEXT NOT NULL,
    verification_status TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
