import java.security.*;
import javax.crypto.*;
import javax.crypto.spec.*;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		String s;
		byte[] dataBytes, digest, seed, digestAppended;
		SecretKey sk;
		MessageDigest md;

		Scanner input = new Scanner(System.in);
		System.out.println("Enter your plaintext:");
		s = input.nextLine();
		dataBytes = s.getBytes();
		
		System.out.println("\nEnter your seed:");
		s = input.nextLine();
		seed = s.getBytes();

		try {
			// QUICK NOTE: SHA-256 message digest length will ALWAYS be 256 bits (64 characters), so use that when decrypting!
			md = MessageDigest.getInstance("SHA-256");
			md.update(dataBytes);
			digest = md.digest();
			System.out.print("\nMessageDigest = ");
			for (byte b: digest) {
				System.out.printf("%02x", Byte.toUnsignedInt(b));
			}
			System.out.println("");
			
			digestAppended = new byte[dataBytes.length + digest.length];
			for (int i = 0; i < digestAppended.length; i++) {
				digestAppended[i] = i < dataBytes.length ? dataBytes[i] : digest[i - dataBytes.length];
			}
			
			// Make AES key generator
			KeyGenerator kg = KeyGenerator.getInstance("AES");
			// Make a SHA-1 pseudo-random number
			SecureRandom rng = SecureRandom.getInstance("SHA1PRNG");
			// Set the seed for our random number generator to be the seed entered by the user
			rng.setSeed(seed);
			// Initialize the key generator by setting the length of the key to be 128 bits (since AES uses 128 length keys)
			kg.init(128, rng);
			// Generate the key
			sk = kg.generateKey();
			System.out.println("\nKEY = " + Base64.getEncoder().encodeToString(sk.getEncoded()));
			
			// Now encrypt digestAppended with sk as the key
			Cipher myCipher = Cipher.getInstance("AES");
			myCipher.init(Cipher.ENCRYPT_MODE, sk);
			byte[] cipherText = myCipher.doFinal(digestAppended);
			
			System.out.println("\nCipher Text = " + Base64.getEncoder().encodeToString(cipherText));
			
			// DECRYPTION TIME!!!
			// Pretend we only have cipherText and seed
			// First, use AES key generator to generate the proper key
			KeyGenerator keyGenDecrypt = KeyGenerator.getInstance("AES");
			SecureRandom rngDecrypt = SecureRandom.getInstance("SHA1PRNG");
			rngDecrypt.setSeed(seed);
			keyGenDecrypt.init(128, rngDecrypt);
			SecretKey skDecrypt = keyGenDecrypt.generateKey();
			System.out.println("\n\nDECRYPTION PROCESS:");
			System.out.println("\nKEY FROM SEED = " + Base64.getEncoder().encodeToString(skDecrypt.getEncoded()));
			
			// Now we have our key (skDecrypt)
			Cipher myCipherDecrypt = Cipher.getInstance("AES");
			myCipherDecrypt.init(Cipher.DECRYPT_MODE, skDecrypt);
			
			byte[] message = myCipherDecrypt.doFinal(cipherText);
			System.out.println("\nORIGINAL MESSAGE = ");
			for (int i = 0; i < message.length - 32; i++) {
				System.out.print((char)message[i]);
			}
			System.out.println("\n\nATTACHED MESSAGE DIGEST = ");
			for (int i = message.length - 32; i < message.length; i++) {
				System.out.printf("%02x", Byte.toUnsignedInt(message[i]));
			}
			
			// Now calculate the message digest, confirm both are the same, then done
			System.out.println("");
			
			
		} catch (NoSuchAlgorithmException e) {
			System.err.println("SHA isn't valid");
		} catch (NoSuchPaddingException e) {
			System.err.println("???");
		} catch (InvalidKeyException e) {
			System.err.println("Invalid key");
		} catch (Exception e){
			System.err.println(e.getMessage());
		}
	}

/*
		try {
			md = MessageDigest.getInstance("SHA");
			md.update(dataBytes);
			digest = md.digest();
			for (byte b: digest) {
				System.out.printf("%02x", Byte.toUnsignedInt(b));
			}
			System.out.println("");
		} catch (NoSuchAlgorithmException e) {
			System.err.println("SHA isn't valid");
		}
	}
*/

}
