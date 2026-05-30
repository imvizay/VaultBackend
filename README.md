# Gallery Vault Backend

A secure FastAPI-powered backend for Gallery Vault, an end-to-end encrypted cloud gallery that follows a zero-knowledge architecture. Images are encrypted entirely on the client before upload, ensuring the server never has access to users' original files or encryption keys.

## Features

* Firebase Authentication & JWT Verification
* End-to-End Encrypted Image Storage
* Zero-Knowledge Architecture
* FastAPI REST API
* PostgreSQL Database Integration
* Cloudinary Raw File Storage
* Secure Metadata Management
* User-Scoped File Access
* Transactional Upload Workflow
* Automatic User Synchronization from Firebase
* SQLAlchemy ORM
* Pydantic Validation
* Production-Ready Service Layer Architecture

## Architecture

Gallery Vault Backend is designed around a zero-knowledge security model:

1. Images are encrypted in the browser using AES-GCM.
2. A master encryption key is derived client-side using Argon2id.
3. Only encrypted blobs are transmitted to the backend.
4. Cloudinary stores encrypted binary data as raw files.
5. PostgreSQL stores metadata such as file information, IVs, ownership, and storage references.
6. Decryption occurs exclusively on the client.

The server never receives:

* User passwords
* Master encryption keys
* Plaintext image data
* Decrypted file content

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Firebase Authentication
* Cloudinary
* Pydantic
* Python

## Security Highlights

* Client-side AES-GCM encryption
* Argon2id key derivation
* Firebase token verification
* User ownership enforcement
* Zero-knowledge file storage
* Secure file metadata handling

## Project Status

Actively under development as part of the Gallery Vault ecosystem.
