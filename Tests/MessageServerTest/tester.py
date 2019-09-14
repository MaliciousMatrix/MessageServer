import unittest
loader = unittest.TestLoader()
start_dir = 'C:\\Users\\Taillow\\Documents\\SoftwareDevelopment\\MessageServer\\MessageServerTest'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
