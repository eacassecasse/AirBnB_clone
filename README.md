<p align="center">
  <i align="center">Manage your app objects easily without a visual interface 🚀</i>
</p>

<h4 align="center">
  <a href="https://python.com/downloads" alt="project language">
        <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    </a>
    <a href="#" alt="Contributors">
        <img alt="GitHub Repo stars" src="https://img.shields.io/github/contributors/eacassecasse/AirBnB_clone?style=for-the-badge">
    </a>
    <a href="#" alt="forks">
        <img alt="GitHub Repo forks" src="https://img.shields.io/github/forks/eacassecasse/AirBnB_clone?style=for-the-badge">
    </a>
    <a href="#" alt="stars">
        <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/eacassecasse/AirBnB_clone?style=for-the-badge">
    </a>
</h4>



<p align="center">
    <img src="https://github.com/amplication/amplication/assets/73097785/c7ed2bbc-8954-46a1-a520-91a4711a9320.png" alt="dashboard"/>
</p>

## Introduction

**HBnB** is a clone of the **AirBnB** service that lets property owner rent out their spaces to travelers looking for
accommodations.
Travelers can rent a space for multiple people to share, a shared space with private rooms, or the entire property for
themselves.<br>

As this project was purposed to cover the fundamental concepts of high level programming, it will implement only some
features
of AirBnB. With that said, it will be composed by: `a command line interpreter`, `a website (the front-end)`
, `a database
or files to store data` and `an API for communitation between front-end and the data`.

At the current stage it will only have a **command line interpreter/console** that will manipulate the data without
having a visual interface, which is perfect for development and debugging purposes. It also allows us to change type of
storage easily without updating our code base that, because we have a storage engine that is managed by each console
command will be implemented

## ⚡️ Quick start

First, [download](https://www.python.org/downloads/) and install **Python**. It is recommended to use the latest Python
version.

Clone the `AirBnB_clone` repository using [`git clone`](https://github.com/eacassecasse/AirBnB_clone.git) command:

```bash
git clone https://github.com/eacassecasse/AirBnB_clone.git
```

Let's open the cloned repository using your terminal, and you'll
ready to **run** this project:

```bash
cd AirBnB_clone
```

Next, run the command line interpreter file (called `console.py`), and you will
be ready to **run** this project:

```bash
$ python console.py
(hbnb)
```

That's all you need to know to start! 🎉

## ⚙️ Commands & Options

### `create`

CLI command for create new instances and save them into a JSON file.
This command takes a `class name` as a required argument and this argument will be used to determine which object will
be created.

On failing to provide the `class name` or providing a non-defined on, the command will return `** class name missing **`
or `** class doesn't exist **` error messages respectively.
<br>

### Usage

```bash
(hbnb) create [class name]
```

| Option       | Description                                       | Type  | Default | Required? |
|--------------|---------------------------------------------------|-------|---------|-----------|
| `class name` | Allows us to choose which object will be created. | `str` | `""`    | Yes       |

```bash
(hbnb) create
"** class name missing **"
(hbnb) create MyModel
"** class doesn't exist **"
(hbnb) create BaseModel
"73a7ae54-3542-4443-bc5e-b94a5381c382"
```

![cgapp_create][cgapp_create_gif]

- 📺 Full demo video: https://recordit.co/OQAwkZBrjN
- 📖 Docs: https://github.com/create-go-app/cli/wiki/Command-create

### `show`

CLI command for displaying an object to the user based on its Identifier.
This command takes a `class name` and a `id` as required arguments and these arguments will be used to determine which
object will be displayed.

On failing to provide any of these arguments (`class name` or `id`) or providing a non-defined `class name`, the command
will return `** class name missing **`, `** class doesn't exist **` or `** instance id missing **`  error messages.

**Return Value**

When you provide the arguments correctly, this command will return either an `object` or a `** no instance found **`
message.
<br>

### Usage

```bash
(hbnb) show [class name] [id]
```

| Option       | Description                                                          | Type  | Default | Required? |
|--------------|----------------------------------------------------------------------|-------|---------|-----------|
| `class name` | Allows us to choose which entities will be fetched.                  | `str` | `""`    | Yes       |
| `id`         | Allows us to choose which instance will be display from the entities | `str` | `""`    | Yes       |

```bash
(hbnb) show
"** class name missing **"
(hbnb) show MyModel
"** class doesn't exist **"
(hbnb) show BaseModel
"** instance id missing **"
(hbnb) show BaseModel 73a7ae54-3542-4443-bc5e-b94a5381c382
"[BaseModel] (73a7ae54-3542-4443-bc5e-b94a5381c382) {'id': '73a7ae54-3542-4443-bc5e-b94a5381c382', 'created_at': datetime.datetime(2024, 1, 12, 13, 52, 33, 825890), 'updated_at': datetime.datetime(2024, 1, 12, 13, 52, 33, 825890)}"
```

![cgapp_create][cgapp_create_gif]

- 📺 Full demo video: https://recordit.co/OQAwkZBrjN
- 📖 Docs: https://github.com/create-go-app/cli/wiki/Command-create

### `all`

CLI command to print all string representations of all the instances based or not on the class name.
This command takes a `class name` as an optional argument and this argument will be used to determine which objects will
be printed.

Note that nothing happens in case of not providing the `class name`, however, if the providing a non-defined the command
will return
a `** class doesn't exist **` error message.
<br>

### Usage

```bash
(hbnb) all [class name]
```

| Option       | Description                                        | Type  | Default | Required? |
|--------------|----------------------------------------------------|-------|---------|-----------|
| `class name` | Allows us to choose which objects will be printed. | `str` | `""`    | No        |

```bash
(hbnb) all
"["[User] (049af956-c59d-4264-a621-6dca790ca609) {'id': '049af956-c59d-4264-a621-6dca790ca609', 'created_at': datetime.datetime(2024, 1, 11, 10, 7, 10, 35293), 'upd
ated_at': datetime.datetime(2024, 1, 11, 11, 52, 32, 422260), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] 
(c4628659-c658-4f42-b198-84d61a5c2528) {'id': 'c4628659-c658-4f42-b198-84d61a5c2528', 'created_at': datetime.datetime(2024, 1, 11, 10, 7, 10, 35293), 'updated_at':
 datetime.datetime(2024, 1, 11, 11, 52, 32, 422260), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[BaseModel] (de059af4-749f-4771-92cc
-48fc866e0270) {'id': 'de059af4-749f-4771-92cc-48fc866e0270', 'created_at': datetime.datetime(2024, 1, 11, 10, 7, 26, 994250), 'updated_at': datetime.datetime(2024
, 1, 11, 11, 52, 32, 422260), 'name': 'My_First_Model', 'my_number': 89}", "[User] (aac88f15-1b08-4912-a463-f5e79cd27865) {'id': 'aac88f15-1b08-4912-a463-f5e79cd27
865', 'created_at': datetime.datetime(2024, 1, 11, 10, 8, 30, 309653), 'updated_at': datetime.datetime(2024, 1, 11, 11, 52, 32, 422260), 'first_name': 'Edmilson', 
'last_name': 'Cassecasse', 'email': 'eacassecasse@hbnb.com', 'password': '@Pas1sword23', 'user': 'eacassecasse'}", "[BaseModel] (e183ed1d-b834-4b06-bb13-a7f4217212
40) {'id': 'e183ed1d-b834-4b06-bb13-a7f421721240', 'created_at': datetime.datetime(2024, 1, 11, 10, 10, 3, 328062), 'updated_at': datetime.datetime(2024, 1, 11, 11
, 51, 4, 199161), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (390d4770-0f23-410a-bd53-b3a44d5568b7) {'id': '390d4770-0f23-410a-bd53-b3a44d5568b7', '
created_at': datetime.datetime(2024, 1, 11, 10, 48, 0, 706692), 'updated_at': datetime.datetime(2024, 1, 11, 10, 48, 0, 706692)}", "[BaseModel] (c3abbf13-1d46-4959
-8b14-427079275e18) {'id': 'c3abbf13-1d46-4959-8b14-427079275e18', 'created_at': datetime.datetime(2024, 1, 11, 10, 50, 29, 542051), 'updated_at': datetime.datetim
e(2024, 1, 11, 10, 50, 29, 542051)}", "[BaseModel] (fa0bdc31-0329-4f6b-a0df-d7c86a73682c) {'id': 'fa0bdc31-0329-4f6b-a0df-d7c86a73682c', 'created_at': datetime.dat
etime(2024, 1, 11, 10, 50, 50, 966957), 'updated_at': datetime.datetime(2024, 1, 11, 10, 50, 50, 966957)}", "[BaseModel] (61be1593-43a4-469b-8cf3-09a7b1e288bc) {'i
d': '61be1593-43a4-469b-8cf3-09a7b1e288bc', 'created_at': datetime.datetime(2024, 1, 11, 10, 51, 4, 203977), 'updated_at': datetime.datetime(2024, 1, 11, 10, 51, 4
, 203977)}", "[BaseModel] (75b1aee5-4198-4b8e-aae4-14870036e7b5) {'id': '75b1aee5-4198-4b8e-aae4-14870036e7b5', 'created_at': datetime.datetime(2024, 1, 11, 10, 51
, 42, 316746), 'updated_at': datetime.datetime(2024, 1, 11, 10, 51, 42, 316746)}", "[BaseModel] (873dfe20-3c02-44d8-a8cc-dc28b5ab045a) {'id': '873dfe20-3c02-44d8-a
8cc-dc28b5ab045a', 'created_at': datetime.datetime(2024, 1, 11, 10, 51, 49, 458733), 'updated_at': datetime.datetime(2024, 1, 11, 10, 51, 49, 458733)}", '[Amenity]
 (a9e5fd04-2ebc-4355-a77a-a023caf2928a) {\'id\': \'a9e5fd04-2ebc-4355-a77a-a023caf2928a\', \'created_at\': datetime.datetime(2024, 1, 11, 14, 46, 13, 433767), \'up
dated_at\': datetime.datetime(2024, 1, 11, 14, 46, 13, 433767), \'name\': \'"kitchen"\'}', "[BaseModel] (5e7ee403-f793-4bda-a361-98afca41eae3) {'id': '5e7ee403-f79
3-4bda-a361-98afca41eae3', 'created_at': datetime.datetime(2024, 1, 11, 16, 35, 26, 825320), 'updated_at': datetime.datetime(2024, 1, 11, 16, 35, 26, 825320)}", "[
BaseModel] (73a7ae54-3542-4443-bc5e-b94a5381c382) {'id': '73a7ae54-3542-4443-bc5e-b94a5381c382', 'created_at': datetime.datetime(2024, 1, 12, 13, 52, 33, 825890), 'updated_at': datetime.datetime(2024, 1, 12, 13, 52, 33, 825890)}"]"
(hbnb) all MyModel
"** class doesn't exist **"
(hbnb) all BaseModel
"["[BaseModel] (de059af4-749f-4771-92cc-48fc866e0270) {'id': 'de059af4-749f-4771-92cc-48fc866e0270', 'created_at': datetime.datetime(2024, 1, 11, 10, 7, 26, 994250)
, 'updated_at': datetime.datetime(2024, 1, 11, 11, 52, 32, 422260), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (e183ed1d-b834-4b06-bb13-a7f421721240
) {'id': 'e183ed1d-b834-4b06-bb13-a7f421721240', 'created_at': datetime.datetime(2024, 1, 11, 10, 10, 3, 328062), 'updated_at': datetime.datetime(2024, 1, 11, 11, 
51, 4, 199161), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (390d4770-0f23-410a-bd53-b3a44d5568b7) {'id': '390d4770-0f23-410a-bd53-b3a44d5568b7', 'cr
eated_at': datetime.datetime(2024, 1, 11, 10, 48, 0, 706692), 'updated_at': datetime.datetime(2024, 1, 11, 10, 48, 0, 706692)}", "[BaseModel] (c3abbf13-1d46-4959-8
b14-427079275e18) {'id': 'c3abbf13-1d46-4959-8b14-427079275e18', 'created_at': datetime.datetime(2024, 1, 11, 10, 50, 29, 542051), 'updated_at': datetime.datetime(
2024, 1, 11, 10, 50, 29, 542051)}", "[BaseModel] (fa0bdc31-0329-4f6b-a0df-d7c86a73682c) {'id': 'fa0bdc31-0329-4f6b-a0df-d7c86a73682c', 'created_at': datetime.datet
ime(2024, 1, 11, 10, 50, 50, 966957), 'updated_at': datetime.datetime(2024, 1, 11, 10, 50, 50, 966957)}", "[BaseModel] (61be1593-43a4-469b-8cf3-09a7b1e288bc) {'id'
: '61be1593-43a4-469b-8cf3-09a7b1e288bc', 'created_at': datetime.datetime(2024, 1, 11, 10, 51, 4, 203977), 'updated_at': datetime.datetime(2024, 1, 11, 10, 51, 4, 
203977)}", "[BaseModel] (75b1aee5-4198-4b8e-aae4-14870036e7b5) {'id': '75b1aee5-4198-4b8e-aae4-14870036e7b5', 'created_at': datetime.datetime(2024, 1, 11, 10, 51, 
42, 316746), 'updated_at': datetime.datetime(2024, 1, 11, 10, 51, 42, 316746)}", "[BaseModel] (873dfe20-3c02-44d8-a8cc-dc28b5ab045a) {'id': '873dfe20-3c02-44d8-a8c
c-dc28b5ab045a', 'created_at': datetime.datetime(2024, 1, 11, 10, 51, 49, 458733), 'updated_at': datetime.datetime(2024, 1, 11, 10, 51, 49, 458733)}", "[BaseModel]
 (5e7ee403-f793-4bda-a361-98afca41eae3) {'id': '5e7ee403-f793-4bda-a361-98afca41eae3', 'created_at': datetime.datetime(2024, 1, 11, 16, 35, 26, 825320), 'updated_a
t': datetime.datetime(2024, 1, 11, 16, 35, 26, 825320)}", "[BaseModel] (73a7ae54-3542-4443-bc5e-b94a5381c382) {'id': '73a7ae54-3542-4443-bc5e-b94a5381c382', 'created_at': datetime.datetime(2024, 1, 12, 13, 52, 33, 825890), 'updated_at': datetime.datetime(2024, 1, 12, 13, 52, 33, 825890)}"]"
```

![cgapp_create][cgapp_create_gif]

- 📺 Full demo video: https://recordit.co/OQAwkZBrjN
- 📖 Docs: https://github.com/create-go-app/cli/wiki/Command-create

### `destroy`

CLI command to delete an object based on the Identifier given by the user.
This command takes a `class name` and a `id` as required arguments and these arguments will be used to determine which
object will be deleted.

On failing to provide any of these arguments (`class name` or `id`) or providing a non-defined `class name`, the command
will return `** class name missing **`, `** class doesn't exist **` or `** instance id missing **`  error messages.

**Return Value**

When you provide the arguments correctly, this command will return either nothing or a `** no instance found **`
message (in case the object trying to be deleted doesn't exist).
<br>

### Usage

```bash
(hbnb) destroy [class name] [id]
```

| Option       | Description                                                          | Type  | Default | Required? |
|--------------|----------------------------------------------------------------------|-------|---------|-----------|
| `class name` | Allows us to choose which entities will be fetched.                  | `str` | `""`    | Yes       |
| `id`         | Allows us to choose which instance will be deleted from the entities | `str` | `""`    | Yes       |

```bash
(hbnb) destroy
"** class name missing **"
(hbnb) destroy MyModel
"** class doesn't exist **"
(hbnb) destroy BaseModel
"** instance id missing **"
(hbnb) destroy BaseModel c377ae54-3542-b4a3-bc5e-b94a5381c381
"** no instance found **"
(hbnb) destroy BaseModel 73a7ae54-3542-4443-bc5e-b94a5381c382
(hbnb) 
```

![cgapp_create][cgapp_create_gif]

- 📺 Full demo video: https://recordit.co/OQAwkZBrjN
- 📖 Docs: https://github.com/create-go-app/cli/wiki/Command-create

### `update`

CLI command to modify an object's attribute based on the identifier and other arguments given by the user.
This command takes a `class name`, an `id`, an `attribute name` and an `attribute value` as required arguments and these
arguments will be used to determine which
object will be modified.

On failing to provide any of these arguments (`class name`, `id`, `attribute name` or `attribute value`) or providing a
non-defined `class name`, the command will return `** class name missing **`, `** class doesn't exist **`
, `** instance id missing **`, `** attribute name missing **` or `** value missing **`  error messages.

**Note that** when you provide the arguments correctly but, the `attribute name` is not an attribute of the instance
object then, it will be created inside the object. Other thing, is that by default this command does not return anything
so to make sure the object was updated you'll have to run the show command for the modified object.
<br>

### Usage

```bash
(hbnb) update [class name] [id] [argument name] [argument value]
```

| Option           | Description                                                            | Type  | Default | Required? |
|------------------|------------------------------------------------------------------------|-------|---------|-----------|
| `class name`     | Allows us to choose which entities will be fetched.                    | `str` | `""`    | Yes       |
| `id`             | Allows us to choose which instance will be modified from the entities. | `str` | `""`    | Yes       |
| `argument name`  | The attribute trying to be modified or to be added to the object.      | `str` | `""`    | Yes       |
| `argument value` | The value for the attribute being modified.                            | `str` | `""`    | Yes       |

```bash
(hbnb) update
"** class name missing **"
(hbnb) update MyModel
"** class doesn't exist **"
(hbnb) update BaseModel
"** instance id missing **"
(hbnb) update BaseModel c377ae54-3542-b4a3-bc5e-b94a5381c381
"** attribute name missing **"
(hbnb) update BaseModel c377ae54-3542-b4a3-bc5e-b94a5381c381 name
"** value missing **"
(hbnb) update BaseModel c377ae54-3542-b4a3-bc5e-b94a5381c381 name Hugo
"** no instance found **"
(hbnb) update BaseModel 390d4770-0f23-410a-bd53-b3a44d5568b7 name Hugo
(hbnb)
```

![cgapp_create][cgapp_create_gif]

- 📺 Full demo video: https://recordit.co/OQAwkZBrjN
- 📖 Docs: https://github.com/create-go-app/cli/wiki/Command-create

### Data Storage

For this stage our data will be stored inside a JSON Files, however, the `FileStorage` module allows us to change the
storage engine whenever we want without re-coding everything.

## 🏆 A win-win cooperation

Despite this project has been developed for study purpose, it can be used as base to create another project.
Thus, if you want some support on the whether you are trying to use this project's code or understand the concepts
behind, feel free to get in touch on any of the channels below! I believe that we can work **together** to
create the **most useful** tools that can help other.

<h4 style="display: flex; flex-direction: row; gap: 0.25rem; justify-content: center" align="center">
  <a href="https://linkedin.com/in/eacassecasse" alt="linkedin">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>
    <a href="https://twitter.com/eacassecasse" alt="X">
        <img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" />
    </a>
    <a href="mailto:edmilsoncassecasse25@gmail.com" alt="email">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
    </a>
    <a href="https://discord.com/eacassecasse" alt="discord">
        <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" />
    </a>
</h4>

You can also:

- Add a [GitHub Star](https://github.com/eacassecasse/AirBnB_clone) to the project.
- [Issues](https://github.com/eacassecasse/AirBnB_clone/issues): ask questions and submit your features.
- [Pull requests](https://github.com/eacassecasse/AirBnB_clone/pulls): send your improvements to the current.

I'm excited to see what we are going to build **together**! 🤩🤩 